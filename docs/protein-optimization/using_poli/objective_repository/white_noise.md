# White Noise objective function

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

This objective function takes any sequence of string integers (e.g. `x=["1", "2", "3"]`) and returns a sample from a standard Gaussian $\mathcal{N}(0, 1)$.

## Prerequisites

None, this function should always run out-of-the-box

## How to run


```python
import numpy as np
from poli import objective_factory

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(name="white_noise")

# Example input:
x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].

# Querying:
print(f(x))
```
