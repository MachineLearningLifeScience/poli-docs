# Bounce

![Type of optimizer algorithm: discrete inputs](https://img.shields.io/badge/Type-discrete_inputs-blue)
[![Bounce (py3.10 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-bounce.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-bounce.yml)

## About

An interface to *Bayesian optimization using increasingly high-dimensional combinatorial and continuous embeddings* (Bounce), by {cite:p}`Papenmeier:Bounce:2024`. This implementation uses [a fork](https://github.com/miguelgondu/bounce) of [the official implementation provided by the authors](https://github.com/LeoIV/bounce).

## How to run

:::{warning}

This solver runs in a different conda environment than base.

You can find a [conda environment where this solver can run here](https://github.com/MachineLearningLifeScience/poli-baselines/blob/main/src/poli_baselines/solvers/bayesian_optimization/bounce/environment.bounce.yml).

If you have cloned `poli-baselines` locally:

```bash
conda env create --file src/poli_baselines/solvers/bayesian_optimization/bounce/environment.bounce.yml
conda activate poli__bounce
```

:::

```python

import numpy as np

from poli import objective_factory
from poli_baselines.solvers.bayesian_optimization.bounce import (
    BounceSolver,
)


problem = objective_factory.create(
    name="rdkit_qed", string_representation="SELFIES"
)
black_box = problem.black_box

# Define the alphabet and sequence length.
# (depending on the problem, you may find them in black_box.info)
alphabet: list[str] = load_your_alphabet()
sequence_length: int = load_your_sequence_length()

solver = BounceSolver(
    black_box=black_box,
    alphabet=alphabet,
    sequence_length=sequence_length,
    n_initial_points=10,
)

solver.solve(max_iter=5)

```

## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Papenmeier, L., Nardi, L., & Poloczek, M. (2024). Bounce: Reliable high-dimensional Bayesian optimization for combinatorial and mixed spaces. arXiv. https://arxiv.org/abs/2307.00618


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@misc{Papenmeier:Bounce:2024,
      title={Bounce: Reliable High-Dimensional Bayesian Optimization for Combinatorial and Mixed Spaces}, 
      author={Leonard Papenmeier and Luigi Nardi and Matthias Poloczek},
      year={2024},
      eprint={2307.00618},
      archivePrefix={arXiv},
      primaryClass={cs.LG}
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



