
# LaMBO2

![Type of optimizer algorithm: proteins only](https://img.shields.io/badge/Type-proteins_only-blue)
[![LaMBO2 (py3.10 in conda)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-lambo2.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing-lambo2.yml)

## About

This is an implementation of LaMBO2 as described in {cite:p}`Gruver:Lambo2:2024`. We use the [official GitHub implementation provided by Genentech](https://github.com/prescient-design/cortex) underneath.

:::{note}
A [tutorial on optimizing thermal stability of RFP proteins](https://github.com/MachineLearningLifeScience/poli-baselines/tree/main/examples/06_running_lambo2_on_rasp) is available in `poli-baselines`' repository.

Another minimal example is [available on Colab](https://colab.research.google.com/drive/1otOBPvzV60_tASkGsfkJ1ng-xogdPWFJ?usp=sharing).
:::

## How to run

:::{warning}

This solver runs in a different conda environment than base. You will have to install `cortex` to run it:

```bash
pip install pytorch-cortex
```

:::

```python
import numpy as np

from poli.objective_repository import EhrlichProblemFactory

from poli_baselines.solvers.bayesian_optimization.lambo2 import (
    LaMBO2,
)

problem = EhrlichProblemFactory().create(
    sequence_length=10,
    motif_length=4,
    n_motifs=2,
    return_value_on_unfeasible=-1.0
)
f, x0 = problem.black_box, problem.x0

solver = LaMBO2(
    black_box=f,
    x0=x0,
)
```

## See more

- By default, `LaMBO2` runs with a conservative set-up for the underlying optimizer. [You can find the configuration here](https://github.com/MachineLearningLifeScience/poli-baselines/tree/main/src/poli_baselines/solvers/bayesian_optimization/lambo2/hydra_configs), and you can override the set-up using the `overrides` kwarg of the solver.
- [Our implementation is based on the 4th tutorial in `cortex`](https://github.com/prescient-design/cortex/tree/main/tutorials).


## References

If you use this solver, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Gruver, N., Stanton, S., Frey, N., Rudner, T. G. J., Hotzel, I., Lafrance-Vanasse, J., Rajpal, A., Cho, K., & Wilson, A. G. (2024). Protein design with guided discrete diffusion. Advances in Neural Information Processing Systems, 36.

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{Gruver:Lambo2:2024,
  title={Protein design with guided discrete diffusion},
  author={Gruver, Nate and Stanton, Samuel and Frey, Nathan and Rudner, Tim GJ and Hotzel, Isidro and Lafrance-Vanasse, Julien and Rajpal, Arvind and Cho, Kyunghyun and Wilson, Andrew G},
  journal={Advances in Neural Information Processing Systems},
  volume={36},
  year={2024}
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

## API reference

```{eval-rst}
.. autoclass:: poli_baselines.solvers.bayesian_optimization.lambo2.LaMBO2
    :members:
```

