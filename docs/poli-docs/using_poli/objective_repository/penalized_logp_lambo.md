# Penalized logP (using `lambo`)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli lambo](https://img.shields.io/badge/Environment-poli____lambo-teal
)

## About

This objective function computes the penalized logP _exactly_ as is done in the `lambo` implementation[^1] {cite:p}`stanton2022accelerating`.

[^1]: If you check carefully, you might have noticed that they add to their implementation the empirical means and standard deviations of the ZINC dataset for the values they compute.

To do so, we import their scoring function.

## Prerequisites

None. This black box should run out-of-the-box.


## How to run

```python
import numpy as np
from poli.objective_repository import (
    PenalizedLogPLamboProblemFactory,
    PenalizedLogPLamboBlackBox,
)

# Creating the black box
f = PenalizedLogPLamboBlackBox()

# Creating a problem
problem = PenalizedLogPLamboProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input: a single carbon
x = np.array(["C"]).reshape(1, -1)

# Querying:
y = f(x)
print(y)  # Should be close to -6.2238
```

## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Stanton, Samuel, Wesley Maddox, Nate Gruver, Phillip Maffettone, Emily Delaney, Peyton Greenside, and Andrew Gordon Wilson. “Accelerating Bayesian Optimization for Biological Sequence Design with Denoising Autoencoders.” arXiv, July 12, 2022. http://arxiv.org/abs/2203.12742.

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{stanton:LaMBO:2022,
  title   = {Accelerating Bayesian Optimization for Biological Sequence Design with Denoising Autoencoders},
  author  = {Stanton, Samuel and Maddox, Wesley and Gruver, Nate and Maffettone, Phillip and Delaney, Emily and Greenside, Peyton and Wilson, Andrew Gordon},
  journal = {arXiv preprint arXiv:2203.12742},
  year    = {2022}
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
