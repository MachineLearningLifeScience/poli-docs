# Optimizing an objective function

```{contents}
```

In this chapter, we combine what we have discussed in the previous two chapters to optimize a black box objective function using `poli` and its baselines. In particular, we'll solve the `aloha` problem using discrete random mutations.

> This tutorial follows `optimizing_aloha.py` in `poli-baselines/examples`.

## Prerequisites

Before running this, you need to make sure you have

- You have both `poli` and `poli_baselines` installed.
- run [the first chapter on registering black box functions](./registering_an_objective_function.md).
- read [the second chapter on implementing solvers](./defining_a_problem_solver.md)

By the end, you should have registered the `aloha` problem.

## Is aloha registered?

We can start by checking that the `aloha` problem is indeed among the registered objectives:

```python
# optimizing_aloha.py
from poli.core.registry import get_problems

if __name__ == "__main__":
    assert "aloha" in get_problems()
```

This script should run without raising any problems.

:::{admonition} Is aloha not registered?
:class: dropdown

If the past snippet fails and raises an `AssertionError`, then it's likely you haven't registered `aloha` as a problem. Check [the first chapter for the process of registering this problem](./registering_an_objective_function.md).

:::

## Instancing the problem and solver

Since the problem is registered, optimizing it is really easy!

```python
# optimizing_aloha.py
from poli import objective_factory
from poli.core.registry import get_problems
from poli_baselines.solvers.simple.random_mutation import RandomMutation

if __name__ == "__main__":
    assert "aloha" in get_problems()

    # Creating an instance of the problem
    problem_info, f, x0, y0, run_info = objective_factory.create(
        name="aloha", caller_info=None, observer=None
    )

    # Creating an instance of the solver
    solver = RandomMutation(
        black_box=f,
        x0=x0,
        y0=y0,
        alphabet=problem_info.get_alphabet(),
    )
```

## Optimizing

Solvers in `poli_baselines` have a `solve` method. Its only required argument is the number of iterations we want to run the optimization for (`max_iters: int`). Other keyword arguments include e.g. `break_at_performance: float = None`, or `verbose: bool = False`.

Once instantiated, the solver can optimize our `aloha` problem easily:

```python
# optimizing_aloha.py

...

if __name__ == "__main__"
    ...
    
    # Running the optimization for 1000 steps,
    # breaking if we find a performance above 5.0, 
    # and printing a small summary at each step.
    solver.solve(max_iter=1000, break_at_performance=5.0, verbose=True)
    print(solver.get_best_solution())
```

Just by running random mutations, you can find the "ALOHA" string in usually less than 1000 random mutations.

## Conclusion

In this tutorial we used `RandomMutations` to optimize a toy example: the `aloha` problem described in [the first chapter](./registering_an_objective_function.md).

This concludes the "Getting Started" section of this tutorial. The key takeaways are these:

1. With `poli`, you can register black box objective functions which, when instantiated, will run on an independent process in a custom environment you specify at registration.
2. `poli_baselines` allows you to define black box optimization algorithms that operate well with `poli`'s registered problems.
3. `poli_baselines` also comes with several solvers, including `RandomMutations`.

The next chapter discusses a more advanced set-up: registering a black-box objective function with Java dependencies, as well as `torch`, and loading up certain autoencoders.
