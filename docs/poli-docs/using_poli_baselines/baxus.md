# Adaptively expanding subspaces (BAxUS)

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)
[![BAxUS (py3.10 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-baxus.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-baxus.yml)

## About

This is an implementation of _Bayesian Optimization with adaptively expanding subspaces_ (BAxUS) as described in {cite:p}`Papenmeier:BAxUS:2022`. This implementation [uses the original open source implementation and Python package developed by the authors](https://github.com/LeoIV/BAxUS).

## How to run

:::{warning}

This solver runs in a different conda environment than base.

You can find a [conda environment where this solver can run here](https://github.com/MachineLearningLifeScience/poli-baselines/blob/main/src/poli_baselines/solvers/bayesian_optimization/baxus/environment.baxus.yml).

:::


```python
import numpy as np

from poli import objective_factory
from poli_baselines.solvers.bayesian_optimization.baxus import BAxUS

problem = objective_factory.create(
    name="toy_continuous_problem",
    function_name="ackley_function_01",
    n_dimensions=10,
)
black_box, x0 = problem.black_box, problem.x0

x0 = np.random.uniform(-1, 1, size=10).reshape(1, 10)
y0 = black_box(x0)

solver = BAxUS(black_box, x0, y0, bounds=(-3.0, 3.0), noise_std=0.0, n_init=2)

solver.solve(max_iter=3)
```

## See more

- The original reference: [*Increasing the Scope as You Learn: Adaptive Bayesian Optimization in Nested Subspaces*](https://proceedings.neurips.cc/paper_files/paper/2022/file/4b7439a4ab0b8e4bcb4e2412c6a10a58-Paper-Conference.pdf).
- [*Taking the human out of the loop*](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf) is a great tutorial of Bayesian Optimization {cite:p}`Shahriari:BOReview:2016`.
- Since `poli` works mostly on discrete inputs, this baseline is implemented with the intention of optimizing in the latent spaces of deep generative models like Generative Adversarial Networks (GANs) or Variational Autoencoders (VAEs) {cite:p}`GomezBombarelli:VAEsAndOpt:2018`.


## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Papenmeier, L., Nardi, L., & Poloczek, M. (2022, May 16). Increasing the Scope as You Learn: Adaptive Bayesian Optimization in Nested Subspaces. Advances in Neural Information Processing Systems. https://openreview.net/forum?id=e4Wf6112DI


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@inproceedings{Papenmeier:BAxUS:2022,
    title={Increasing the Scope as You Learn: Adaptive Bayesian Optimization in Nested Subspaces},
    url={https://openreview.net/forum?id=e4Wf6112DI},
    author={Papenmeier, Leonard and Nardi, Luigi and Poloczek, Matthias},
    year={2022},
    month=may,
    language={en}
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


