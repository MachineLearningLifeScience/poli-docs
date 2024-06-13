# Adding a new optimizer to `poli-baselines`

The main use-case for `poli_baselines` is **defining optimizers for objective functions** defined in `poli`.

The main design objective of `poli` is for it to be almost trivial to **query** complicated black box objective functions; likewise, the design objective of `poli_baselines` is to allow developers of black-box optimization algorithms to benchmark them on said objective functions.  

This chapter explains how to define a "solver", or a black-box optimization algorithm.

:::{note}

By default, all our optimizers **maximize**.

:::

## An abstract problem solver

All problem solvers in `poli_baselines` inherit from an `AbstractSolver`, which is implemented as follows:

```python
# poli_baselines/core/abstract_solver.py
class AbstractSolver:
    def __init__(
        self,
        black_box: AbstractBlackBox,
        x0: np.ndarray | None = None,
        y0: np.ndarray | None = None,
    ):
        self.black_box = black_box
        self.x0 = x0
        self.y0 = y0
```

i.e. the minimal ingredients required to instantiate a solver are a black-box function defined through `poli`, the initial design `x0`, and its evaluation `y0`.

**The only abstract method required** is a `solve`, in which you can implement all the complex logic required to optimize the objective function for `max_iter: int` iterations.

```python
# poli_baselines/core/abstract_solver.py
class AbstractSolver:
    ...

    def solve(
        self,
        max_iter: int = 100,
        n_initial_points: int = 0,
        seed: int | None = None,
    ) -> None:
        """
        Optimizes the problem for a given number of iterations.

        Logging of the black box calls is usually handled by
        poli and their observers.

        Parameters
        ----------
        max_iter: int, optional
            The maximum number of iterations to run. By default, 100.
        n_initial_points: int, optional
            The number of initial points to evaluate before starting
            the optimization. By default, 0 (since initialization
            is usually handled by passing x0 and y0 to the solver)
        seed: int, optional
            The seed to use for the random number generator. By default,
            None, which means that no seed is set.
        """
        raise NotImplementedError
```

Some solvers out there don't allow for imposing an initial condition. In those cases, you can usually pass a `n_initial_points` instead, and leave `x0 = None` and `y0 = None` in the initialization.


## An example: `RandomMutations`

Leveraging the fact that we are usually working with discrete sequences, we can implement the simplest version of an optimizer: one that takes the best performing sequence, and randomly mutates one of its positions.

The following is an implementation of exactly this:

```python
# poli_baselines/solvers/simple/random_mutation.py (almost)
class RandomMutation(AbstractSolver):
    def __init__(
        self,
        black_box: AbstractBlackBox,
        x0: np.ndarray,
        y0: np.ndarray,
    ):
        super().__init__(black_box, x0, y0)

        # Storing the history
        self.history = {
            "x": [x0_i.reshape(1, -1) for x0_i in x0],
            "y": [y0_i.reshape(1, -1) for y0_i in y0],
        }

        self.alphabet = black_box.info.alphabet
        self.alphabet_size = len(self.alphabet)

    def next_candidate(self) -> np.ndarray:
        """
        Returns the next candidate solution
        after checking the history.

        In this case, the RandomMutation solver
        simply returns a random mutation of the
        best performing solution so far.
        """
        # Get the best performing solution so far
        best_x = self.history["x"][np.argmax(self.history["y"])]

        # Perform a random mutation
        # (Assuming that x is always [1, L] in shape)
        next_x = best_x.copy()
        pos = np.random.randint(0, len(next_x.flatten()))
        mutant = np.random.choice(self.alphabet)
        next_x[0][pos] = mutant

        return next_x
    
    def solve(self, max_iter: int, n_initial_points: int = 0, seed: int = None):
        if seed is not None:
            # then seed everything...
            np.random.seed(seed)
        
        for _ in range(max_iter):
            # Evaluate
            x = self.next_candidate()
            y = self.black_box(x)

            # and update the history
            self.history["x"] += [x_i.reshape(1, -1) for x_i in x]
            self.history["y"] += [y_i.reshape(1, -1) for y_i in y]
```

Pretty lean! Notice how **the `solve` method could perform all sorts of complicated logic** like latent space Bayesian Optimization, evolutionary algorithms... The main reason for us to only ask for `solve` to be implemented is to allow practitioners to quickly pipe in their own implementations.

Moreover, the conda environment where you do the optimization has nothing to do with the environment where the objective function was defined: `poli` is set up in such a way that you can query the objective functions without having to worry!

:::{note}
Our implementation of `RandomMutation` is slightly different, since we allow users to query e.g. integer indices instead of strings. It also uses a `StepByStepSolver` in which you would only have to implement the `next_candidate` method.

[Take a look at the exact implementation on `poli_baselines/solvers/simple/random_mutation.py`](https://github.com/MachineLearningLifeScience/poli-baselines/blob/main/src/poli_baselines/solvers/simple/random_mutation.py).
:::

## Submitting a pull request

If you want to share your optimizer with us, feel free to create a pull request in our repository following these instructions:

First, create a fork of [`poli-baselines`](https://github.com/MachineLearningLifeScience/poli-baselines).

Secondly, add a new subfolder in the `solvers` folder following this structure:

```bash
# In poli-baselines' solvers folder
solvers
├── ...
├── your_solver_name
│   ├── __init__.py
│   ├── environment.your_solver_name.yml
│   └── your_solver_name.py
```

If your solver needs a special set of requirements, we expect you to add a conda environment `environment.your_solver_name.yml` in which `your_solver_name.py` could be imported. See a template here:

```yml
name: poli__your_solver_name
channels:
  - defaults
dependencies:
  - python=3.10
  - pip
  - pip:
      - your
      - dependencies
      - here
      - "git+https://github.com/MachineLearningLifeScience/poli.git@dev"
      - "git+https://github.com/MachineLearningLifeScience/poli-baselines.git@main"
```

Ideally, you would also add a couple of tests in the relevant subfolder of `tests`. Feel free to pattern-match from other solvers.

Finally, you can test your solver using something a toy function:

```python
from poli.repository import AlohaProblemFactory
from poli_baselines.solvers.your_solver_name import YourSolver

# Define the toy-est of toy functions
problem = AlohaProblemFactory().create()
black_box, x0 = problem.black_box, problem.x0

# Create an instance of your solver
your_solver = YourSolver(
    black_box=black_box,
    x0=x0,
    y0=black_box(x0),
)

# Optimize for a given number of iterations.
your_solver.solve(10)
```

Once you know your optimizer works in this setting, you can **submit a pull-request** to `poli-baselines`.
