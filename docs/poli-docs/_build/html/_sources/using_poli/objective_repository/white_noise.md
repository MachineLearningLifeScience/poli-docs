# White Noise objective function

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

This objective function takes any sequence of string integers (e.g. `x=["1", "2", "3"]`) and returns a sample from a standard Gaussian $\mathcal{N}(0, 1)$.

## Prerequisites

None, this function should always run out-of-the-box

## Black box information

```python
BlackBoxInformation(
    name="white_noise",
    max_sequence_length=np.inf,
    aligned=False,
    fixed_length=False,
    deterministic=False,
    alphabet=[str(i) for i in range(10)],
    log_transform_recommended=False,
    discrete=True,
    padding_token="",
)
```

## How to run


```python
import numpy as np
from poli.objective_repository import WhiteNoiseProblemFactory, WhiteNoiseBlackBox

# Creating the black box
f = WhiteNoiseBlackBox()

# Creating a problem
problem = WhiteNoiseProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input:
x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].

# Querying:
print(f(x))
```

## How to cite


If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

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

