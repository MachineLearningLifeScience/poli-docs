# Objective function name

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli base](https://img.shields.io/badge/Environment-poli____base-teal
)

## About

...

## Prerequisites

None

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In current environment

```python
import numpy as np
from poli import objective_factory

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(name="problem_name")

# Example input:
x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].

# Querying:
print(f(x))
```

:::

:::{tab-item} In isolation

If you are interested in debugging locally, clone and install as follows: 

```bash
import numpy as np
from poli import objective_factory

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(name="problem_name")

# Example input:
x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].

# Querying:
print(f(x))
```

:::

::::

## See also

- [an internal link of sorts]()
