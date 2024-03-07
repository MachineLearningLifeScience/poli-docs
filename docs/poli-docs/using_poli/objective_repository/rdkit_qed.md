# Quantitative Estimate of Druglikeness (QED)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli chem](https://img.shields.io/badge/Environment-poli____chem-teal
)

## About

This objective function returns the Quantitative Estimate of Druglikeness (QED) using `RDKit`. You can specify whether you are measuring the QED of a SMILES string, or a SELFIES.

## Prerequisites

None. This black box should work out-of-the-box.

## How to run


```python
import numpy as np
from poli.objective_repository import QEDProblemFactory, QEDBlackBox

# Creating the black box
f = QEDBlackBox(string_representation="SELFIES")

# Creating a problem
problem = QEDProblemFactory().create(string_representation="SELFIES")
f, x0 = problem.black_box, problem.x0

# Example input: a single carbon
x = np.array([["[C]"]])

# Querying:
y = f(x)
print(y)  # Should be close to 0.35978
```
