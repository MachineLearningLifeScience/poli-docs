# Probabilistic Reparametrization

![Type of optimizer algorithm: discrete inputs](https://img.shields.io/badge/Type-discrete_inputs-blue)
[![Prob. Rep. (py3.10 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-pr.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-pr.yml)

## About

An interface to *Bayesian optimization with Probabilistic Reparametrization* (ProbRep), by {cite:p}`Daulton:ProbRep:2022`. This implementation uses [a fork](https://github.com/miguelgondu/bo_pr) of [the official implementation provided by the authors](https://github.com/facebookresearch/bo_pr).

## How to run

:::{warning}

This solver runs in a different conda environment than base.

You can find a [conda environment where this solver can run here](https://github.com/MachineLearningLifeScience/poli-baselines/blob/main/src/poli_baselines/solvers/bayesian_optimization/pr/environment.pr.yml).

If you have cloned `poli-baselines` locally:

```bash
conda env create --file src/poli_baselines/solvers/bayesian_optimization/pr/environment.pr.yml
conda activate poli__pr
```

:::

```python

import numpy as np

from poli import objective_factory
from poli_baselines.solvers.bayesian_optimization.pr import (
    ProbabilisticReparametrizationSolver,
)

# Define the alphabet and sequence length.
# (depending on the problem, you may find them in black_box.info)
alphabet: list[str] = load_alphabet()
sequence_length: int = load_sequence_length()

problem = objective_factory.create(
    name="rdkit_qed", string_representation="SELFIES"
)
black_box, x0 = problem.black_box, problem.x0
y0 = black_box(x0)

# Add padding to complete the original input to the sequence length
x0_ = np.array([["[nop]"] * sequence_length])
x0_[0, : x0.shape[1]] = x0

solver = ProbabilisticReparametrizationSolver(
    black_box=black_box,
    x0=x0_,
    y0=y0,
    alphabet=alphabet,
    sequence_length=sequence_length,
)

solver.solve(max_iter=10)
```

## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Daulton, S., Wan, X., Eriksson, D., Balandat, M., Osborne, M. A., & Bakshy, E. (2022). Bayesian optimization over discrete and mixed spaces via probabilistic reparameterization. In Advances in Neural Information Processing Systems 35.


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@inproceedings{Daulton:ProbRep:2022,
      title={Bayesian Optimization over Discrete and Mixed Spaces via Probabilistic Reparameterization}, 
      author={Samuel Daulton and Xingchen Wan and and David Eriksson and Maximilian Balandat and Michael A. Osborne and Eytan Bakshy},
      booktitle={Advances in Neural Information Processing Systems 35},
      year={2022}
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



