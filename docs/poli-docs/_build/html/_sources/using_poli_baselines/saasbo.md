# Sparse Axis-Aligned Subspaces Bayesian Optimization (SAASBO)

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)
[![Ax (py3.10 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-ax.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-ax.yml) 

## About


This is an implementation of _Sparse Axis-Aligned Subspaces_ Bayesian Optimization (SAASBO), proposed in {cite:p}`Eriksson:saasbo:2021`.

SAAS corresponds to a certain Gaussian Process model, in which lengthscales have priors that encourage sparcity. Moreover, the authors encourage a fully Bayesian treatment and thus rely on No U-turn Sampling (NUTS).

## How to run

:::{warning}

This solver runs in a different conda environment than base.

You can find a [conda environment where this solver can run here](https://github.com/MachineLearningLifeScience/poli-baselines/blob/fb7d3b6f48c58d05c114cab4ff45b8f5c02428c5/src/poli_baselines/core/utils/ax/environment.ax.yml#L1).

:::

```python
import numpy as np

from poli.objective_repository import ToyContinuousBlackBox

from poli_baselines.solvers.bayesian_optimization.saasbo import SAASBO

f_ackley = ToyContinuousBlackBox(function_name="ackley_function_01", n_dimensions=2)

x0 = np.random.randn(2).reshape(1, -1).clip(-2.0, 2.0)
y0 = f_ackley(x0)

bo_solver = SAASBO(
    black_box=f_ackley,
    x0=x0,
    y0=y0,
)

bo_solver.solve(max_iter=10)
```

## See more

- [*Taking the human out of the loop*](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf) is a great tutorial of Bayesian Optimization {cite:p}`Shahriari:BOReview:2016`.
- Since `poli` works mostly on discrete inputs, this baseline is implemented with the intention of optimizing in the latent spaces of deep generative models like Generative Adversarial Networks (GANs) or Variational Autoencoders (VAEs) {cite:p}`GomezBombarelli:VAEsAndOpt:2018`.
