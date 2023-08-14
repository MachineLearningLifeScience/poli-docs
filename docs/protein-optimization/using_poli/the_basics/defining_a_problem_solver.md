# Defining a problem solver in `poli_baselines`

```{contents}
```

The main use-case for `poli_baselines` is **defining solvers for objective functions**.

The main design objective of `poli` is for it to be almost trivial to **query** complicated black box objective functions; likewise, the design objective of `poli_baselines` is to allow developers of black-box optimization algorithms to test them on said objective functions.  

This chapter explains how to define a "solver", or a black-box optimization algorithm.

## An abstract problem solver

All problem solvers in `poli_baselines` inherit from an `AbstractSolver`, which is implemented as follows:

```python
# poli_baselines/core/abstract_solver.py
class AbstractSolver:
    def __init__(
        self,
        black_box: AbstractBlackBox,
        x0: np.ndarray,
        y0: np.ndarray,
    ):
        self.black_box = black_box
        self.x0 = x0
        self.y0 = y0

        self.history = {
            "x": [x0],
            "y": [y0],
        }
```

i.e. the minimal ingredients required to instantiate a solver are a black-box function defined through `poli`, the initial design `x0`, and its evaluation `y0`.

**The only abstract method required** of the user is a `next_candidate() -> np.ndarray`, which uses the `self.history` to propose a new candidate. Using this method, the abstract solver implements a `.solve(max_iter: int)` as follows:

```python
# poli_baselines/core/abstract_solver.py
class AbstractSolver:
    ...

    def next_candidate(self) -> np.ndarray:
        """
        Returns the next candidate solution
        after checking the history.
        """
        raise NotImplementedError(
            "This method is abstract, and should be implemented by a subclass."
        )

    def solve(self, max_iter: int = 100):
        """
        Runs the solver for the given number of iterations.
        """
        for i in range(max_iter):
            # Query the next candidate
            x = self.next_candidate()

            # Evaluate on the black box
            y = self.black_box(x)

            # Add to history
            self.history["x"].append(x)
            self.history["y"].append(y)
```


:::{admonition} What about batched candidates?
:class: dropdown

Batched inputs are not supported yet in `poli`. It's work in progress!

:::

## An example: `RandomMutations`

Leveraging the fact that we're working with discrete sequences, we can implement the simplest version of an optimizer: one that takes the best performing sequence, and randomly mutates one of its positions.

The following is an implementation of exactly this:

```python
# poli_baselines/solvers/simple/random_mutation.py
class RandomMutation(AbstractSolver):
    def __init__(
        self,
        black_box: AbstractBlackBox,
        x0: np.ndarray,
        y0: np.ndarray,
        alphabet_size: int,
    ):
        super().__init__(black_box, x0, y0)
        self.alphabet_size = alphabet_size

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
        next_x[0][pos] = np.random.randint(0, self.alphabet_size)

        return next_x
```

Pretty lean! Notice how **the `next_candidate` method could perform all sorts of complicated logic** like latent space Bayesian Optimization, evolutionary algorithms... Moreover, the conda environment where you do the optimization has nothing to do with the enviroment where the objective function was defined: `poli` is set up in such a way that you can query the objective functions without having to worry!

In the next chapter, we apply this solver to the `aloha` problem we defined in [the first chapter](./registering_an_objective_function.md).
