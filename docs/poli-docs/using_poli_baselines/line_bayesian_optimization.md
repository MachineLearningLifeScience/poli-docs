# Line Bayesian Optimization

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)

## About

Line Bayesian Optimization (LineBO) is a version of [Bayesian Optimization](./bayesian_optimization.md) that restricts the optimization of the acquisition function to a single line in input space {cite:p}`Kirschner:LineBO:2019`. This line can either be selected at random, or can follow one of the coordinate directions.

By default, we use `botorch`'s `SingleTaskGP` {cite:p}`Balandat:botorch:2020`. 

## How to run

```python
import numpy as np

from poli.objective_repository import ToyContinuousBlackBox

from poli_baselines.solvers import LineBO

n_dimensions = 3
population_size = 10

f = ToyContinuousBlackBox(
    function_name="ackley_function_01",
    n_dimensions=n_dimensions,
)

x0 = np.random.randn(2).reshape(1, -1).clip(-2.0, 2.0)
y0 = f(x0)

solver = LineBO(
    black_box=f,
    x0=x0,
    y0=y0,
    type_of_line="random",  # could also be "coordinate"
)

solver.solve(max_iter=10)
```
