# Adding a new optimizer to `poli-baselines`

The main use-case for `poli_baselines` is **defining optimizers for objective functions**.

The main design objective of `poli` is for it to be almost trivial to **query** complicated black box objective functions; likewise, the design objective of `poli_baselines` is to allow developers of black-box optimization algorithms to test them on said objective functions.  

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
        x0: np.ndarray,
        y0: np.ndarray,
    ):
        self.black_box = black_box
        self.x0 = x0
        self.y0 = y0

        self.history = {
            "x": [x0_i.reshape(1, -1) for x0_i in x0],
            "y": [y0_i.reshape(1, -1) for y0_i in y0],
        }

        self.iteration = 0
```

i.e. the minimal ingredients required to instantiate a solver are a black-box function defined through `poli`, the initial design `x0`, and its evaluation `y0`.

**The only abstract method required** is a `next_candidate() -> np.ndarray`, which uses the `self.history` to propose a new candidate. Using this method, the abstract solver implements a `.solve(max_iter: int)` as follows:

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
            # Call the pre-step callbacks
            if pre_step_callbacks is not None:
                for callback in pre_step_callbacks:
                    callback(self)

            # Take a step, which in turn updates the local history.
            _, y = self.step()

            # Call the post-step callbacks
            if post_step_callbacks is not None:
                for callback in post_step_callbacks:
                    callback(self)

            if verbose:
                print(f"Iteration {i}: {y}, best so far: {self.get_best_performance()}")

            if break_at_performance is not None:
                if y >= break_at_performance:
                    break
```

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
```

Pretty lean! Notice how **the `next_candidate` method could perform all sorts of complicated logic** like latent space Bayesian Optimization, evolutionary algorithms... Moreover, the conda environment where you do the optimization has nothing to do with the enviroment where the objective function was defined: `poli` is set up in such a way that you can query the objective functions without having to worry!

:::{note}
Our implementation of `RandomMutation` is slightly different, since we allow users to query e.g. integer indices instead of strings.

[Take a look at the exact implementation on `poli_baselines/solvers/simple/random_mutation.py`](https://github.com/MachineLearningLifeScience/poli-baselines/blob/main/src/poli_baselines/solvers/simple/random_mutation.py).
:::

## Submitting a pull request

If you want to share your problem with us, feel free to create a pull request in our repository following the instructions in our `CONTRIBUTING.md`: https://github.com/MachineLearningLifeScience/poli-baselines
