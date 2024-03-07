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
