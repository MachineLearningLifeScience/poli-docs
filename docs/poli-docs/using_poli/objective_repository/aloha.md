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
