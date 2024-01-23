# CMA-ES

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)

## About

Covariance Matrix Adaptation - Evolutionary Strategy (CMA-ES) maintains the mean $\boldsymbol{\mu}$ and the covariance $\boldsymbol{\Sigma}$ of a Normal distribution, updating it using a subset of the best-performing members at each iteration {cite:p}`Hansen:CMA-ES:1996`.

For an introduction to evolutionary strategies we recommend [this blogpost by David Ha](https://blog.otoro.net/2017/10/29/visual-evolution-strategies/).

In our implementation, we use `pycma`.

## How to run

```python
from poli_baselines.solvers import CMA_ES
from poli.objective_repository import ToyContinuousProblemFactory

n_dimensions = 3
population_size = 10

problem_factory = ToyContinuousProblemFactory()

f, _, _ = problem_factory.create(
    name="toy_continuous_problem",
    function_name="ackley_function_01",
    n_dimensions=n_dimensions,
)

x0 = np.random.normal(size=(population_size, n_dimensions))
y0 = f(x0)

initial_mean = np.random.normal(size=n_dimensions)
solver = CMA_ES(
    black_box=f,
    x0=x0,
    y0=y0,
    initial_mean=initial_mean,
    initial_sigma=1.0,
    population_size=population_size,
)

solver.solve(max_iter=50)
```
