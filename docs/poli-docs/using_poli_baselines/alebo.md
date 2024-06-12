# Adaptive Linear Embedding Bayesian Optimization (ALEBO)

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)
[![Ax (py3.10 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-ax.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-ax.yml) 

## About

This is an implementation of _Adaptive Linear Embeddings_ (ALEBO) as described in {cite:p}`Letham:ALEBO:2020`. We use [the model provided by Ax](https://ax.dev/api/_modules/ax/modelbridge/strategies/alebo.html).

## How to run

:::{warning}

This solver runs in a different conda environment than base.

You can find a [conda environment where this solver can run here](https://github.com/MachineLearningLifeScience/poli-baselines/blob/fb7d3b6f48c58d05c114cab4ff45b8f5c02428c5/src/poli_baselines/core/utils/ax/environment.ax.yml#L1).

:::

```python
import numpy as np

from poli.objective_repository import ToyContinuousBlackBox

from poli_baselines.solvers.bayesian_optimization.alebo import (
    ALEBO,
)


f_ackley = ToyContinuousBlackBox(function_name="ackley_function_01", n_dimensions=10)

x0 = np.random.randn(10).reshape(1, -1).clip(-2.0, 2.0)
y0 = f_ackley(x0)

bo_solver = ALEBO(
    black_box=f_ackley,
    x0=x0,
    y0=y0,
    lower_dim=2,  # It's necessary to specify the assumed effective dim.
)

bo_solver.solve(max_iter=10)
```

## See more

- The original reference: [*Re-Examining Linear Embeddings for High-Dimensional Bayesian Optimization*](https://proceedings.neurips.cc/paper/2020/file/10fb6cfa4c990d2bad5ddef4f70e8ba2-Paper.pdf).
- [*Taking the human out of the loop*](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf) is a great tutorial of Bayesian Optimization {cite:p}`Shahriari:BOReview:2016`.
- Since `poli` works mostly on discrete inputs, this baseline is implemented with the intention of optimizing in the latent spaces of deep generative models like Generative Adversarial Networks (GANs) or Variational Autoencoders (VAEs) {cite:p}`GomezBombarelli:VAEsAndOpt:2018`.


## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Letham, B., Calandra, R., Rai, A., & Bakshy, E. (2020). Re-Examining Linear Embeddings for High-Dimensional Bayesian Optimization. Advances in Neural Information Processing Systems, 33, 1546–1558. https://proceedings.neurips.cc/paper/2020/hash/10fb6cfa4c990d2bad5ddef4f70e8ba2-Abstract.html


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@inproceedings{Letham:ALEBO:2020,
     title={Re-Examining Linear Embeddings for High-Dimensional Bayesian Optimization},
     volume={33},
     url={https://proceedings.neurips.cc/paper/2020/hash/10fb6cfa4c990d2bad5ddef4f70e8ba2-Abstract.html},
     booktitle={Advances in Neural Information Processing Systems},
     publisher={Curran Associates, Inc.},
     author={Letham, Ben and Calandra, Roberto and Rai, Akshara and Bakshy, Eytan},
     year={2020},
     pages={1546–1558}
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

