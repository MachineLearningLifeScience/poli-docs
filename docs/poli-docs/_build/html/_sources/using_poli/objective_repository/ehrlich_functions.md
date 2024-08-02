# Ehrlich functions

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

Ehrlich functions, proposed by {cite:p}`Stanton:Ehrlich:2024`, are a closed-form optimization objective for discrete sequences. They are maximized when a collection of motifs are fulfilled in the input. Check the details in their paper.

## Prerequisites

None, this black box runs out of the box.

## How to run

```python
from poli.objective_repository import EhrlichBlackBox, EhrlichProblemFactory

# You can either
# (i) Create a black box
f = EhrlichBlackBox(
    sequence_length=256,
    motif_length=8,
    n_motifs=4,
    quantization=8,
)

# or
# (ii) create a problem
problem = EhrlichProblemFactory().create(
    sequence_length=256,
    motif_length=8,
    n_motifs=4,
    quantization=8,
)
f, x0 = problem.black_box, problem.x0

# Example input:
print(x0)

# Querying:
y = f(x0)
print(y)
```

## How to cite

::::{tab-set}

:::{tab-item} References as text

[1] Stanton, S., Alberstein, R., Frey, N., Watkins, A., & Cho, K. (2024). Closed-form test functions for biophysical sequence optimization algorithms. arXiv. https://arxiv.org/abs/2407.00236

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@misc{Stanton:Ehrlich:2024,
      title={Closed-Form Test Functions for Biophysical Sequence Optimization Algorithms}, 
      author={Samuel Stanton and Robert Alberstein and Nathan Frey and Andrew Watkins and Kyunghyun Cho},
      year={2024},
      eprint={2407.00236},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2407.00236}, 
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
.. autoclass:: poli.objective_repository.ehrlich.register.EhrlichProblemFactory
    :members:

.. autoclass:: poli.objective_repository.ehrlich.register.EhrlichBlackBox
    :members:
```