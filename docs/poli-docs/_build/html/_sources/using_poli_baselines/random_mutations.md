# Random mutations

![Type of optimizer algorithm: discrete inputs](https://img.shields.io/badge/Type-discrete_inputs-blue)

## About

This optimizer samples a random location of a string in the history, and replaces it with a randomly sampled token from the alphabet.

## How to run

```python

import numpy as np

from poli.objective_repository import AlohaProblemFactory
from poli_baselines.solvers import RandomMutation

problem_factory = AlohaProblemFactory()

problem = problem_factory.create()
f, x0 = problem.black_box, problem.x0
y0 = f(x0)

solver = RandomMutation(
    black_box=f,
    x0=x0,
    y0=y0,
)

solver.solve(max_iter=100)

print(solver.get_best_solution())

```
