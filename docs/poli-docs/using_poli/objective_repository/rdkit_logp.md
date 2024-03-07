# Log-solubility (logP)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli chem](https://img.shields.io/badge/Environment-poli____chem-teal
)

## About

This objective function returns the partition coefficient of a solute between octanol and water (known as logP) using `RDKit`. You can specify whether you are measuring the logP of a SMILES string, or a SELFIES.

## Prerequisites

None. This black box should work out-of-the-box.

## How to run

```python
import numpy as np
from poli.objective_repository import LogPProblemFactory, LogPBlackBox

# Creating the black box
f = LogPBlackBox(string_representation="SMILES")

# Creating a problem
problem = LogPProblemFactory().create(string_representation="SMILES")
f, x0 = problem.black_box, problem.x0

# Example input: a single carbon
x = np.array(["C"]).reshape(1, -1)

# Querying:
y = f(x)
print(y)  # Should be close to 0.6361
```
