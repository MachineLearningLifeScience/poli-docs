# Trust Region Bayesian Optimization (Turbo)

![Type of optimizer algorithm: continuous inputs](https://img.shields.io/badge/Type-continuous_inputs-cyan)
[![Base (python 3.9 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing.yml) 

## About

This is an implementation of _Trust Region Bayesian Optimization_ (Turbo) as described in {cite:p}`Eriksson:Turbo:2019`. This implementation [is based on the Turbo tutorial of botorch](https://botorch.org/tutorials/turbo_1).

## How to run

```python
import numpy as np

from poli.objective_repository import ToyContinuousBlackBox

from poli_baselines.solvers.bayesian_optimization.turbo import (
    Turbo,
)


f_ackley = ToyContinuousBlackBox(function_name="ackley_function_01", n_dimensions=10)

x0 = np.random.randn(10).reshape(1, -1).clip(-2.0, 2.0)
y0 = f_ackley(x0)

bo_solver = Turbo(
    black_box=f_ackley,
    x0=x0,
    y0=y0,
)

bo_solver.solve(max_iter=10)
```

## See more

- The original reference: [*Scalable Global Optimization via Local Bayesian Optimization*](https://proceedings.neurips.cc/paper_files/paper/2019/file/6c990b7aca7bc7058f5e98ea909e924b-Paper.pdf).
- [*Taking the human out of the loop*](https://www.cs.ox.ac.uk/people/nando.defreitas/publications/BayesOptLoop.pdf) is a great tutorial of Bayesian Optimization {cite:p}`Shahriari:BOReview:2016`.
- Since `poli` works mostly on discrete inputs, this baseline is implemented with the intention of optimizing in the latent spaces of deep generative models like Generative Adversarial Networks (GANs) or Variational Autoencoders (VAEs) {cite:p}`GomezBombarelli:VAEsAndOpt:2018`.


## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Eriksson, D., Pearce, M., Gardner, J., Turner, R. D., & Poloczek, M. (2019). Scalable Global Optimization via Local Bayesian Optimization. Advances in Neural Information Processing Systems, 32. https://proceedings.neurips.cc/paper/2019/hash/6c990b7aca7bc7058f5e98ea909e924b-Abstract.html

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@inproceedings{Eriksson:Turbo:2019,
    title={Scalable Global Optimization via Local Bayesian Optimization},
    volume={32},
    url={https://proceedings.neurips.cc/paper/2019/hash/6c990b7aca7bc7058f5e98ea909e924b-Abstract.html},
    booktitle={Advances in Neural Information Processing Systems},
    publisher={Curran Associates, Inc.},
    author={Eriksson, David and Pearce, Michael and Gardner, Jacob and Turner, Ryan D and Poloczek, Matthias},
    year={2019}
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


