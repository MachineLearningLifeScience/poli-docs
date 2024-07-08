# Line Bayesian Optimization

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-red)

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

## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Kirschner, J., Mutny, M., Hiller, N., Ischebeck, R., & Krause, A. (2019). Adaptive and safe Bayesian optimization in high dimensions via one-dimensional subspaces. In Proceedings of the 36th International Conference on Machine Learning (pp. 3429–3438). PMLR. https://proceedings.mlr.press/v97/kirschner19a.html

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@inproceedings{Kirschner:LineBO:2019,
  title = {Adaptive and Safe Bayesian Optimization in High Dimensions via
           One-Dimensional Subspaces},
  ISSN = {2640-3498},
  url = {https://proceedings.mlr.press/v97/kirschner19a.html},
  booktitle = {Proceedings of the 36th International Conference on Machine
               Learning},
  publisher = {PMLR},
  author = {Kirschner, Johannes and Mutny, Mojmir and Hiller, Nicole and
            Ischebeck, Rasmus and Krause, Andreas},
  year = {2019},
  month = may,
  pages = {3429–3438},
  language = {en},
}


@software{Gonzalez-Duque:poli:2024,
author = {González-Duque, Miguel and Bartels, Simon and Michael, Richard},
month = jan,
title = {{poli: a libary of discrete sequence objectives}},
url = {https://github.com/MachineLearningLifeScience/poli},
version = {0.0.1},
year = {2024}
}

```

:::

::::



