# Aloha objective function

![Type of objective function: discrete](https://img.shields.io/badge/Input_type-discrete-blue)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

This toy objective function takes 5-letter sequences (in all-caps) and returns the distance to the string "ALOHA".

## Prerequisites

None, this function should always run out-of-the-box

## How to run

```python
import numpy as np
from poli.objective_repository import AlohaProblemFactory, AlohaBlackBox

# Creating the black box
f = AlohaBlackBox()

# Creating a problem
problem = AlohaProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input:
x = np.array(
    [["A", "L", "O", "O", "F"]]
)  # must be of shape [b, L], in this case [1, 5].

# Querying:
print(f(x))  # Should be 3 (A, L, and the first O).
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
