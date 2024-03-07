# Synthetic Accessibility (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli lambo](https://img.shields.io/badge/Environment-poli____lambo-teal
)

## About

This objective function computes the synthetic accesibility of a small molecule using [the Therapeutics Data Common's oracle](https://tdcommons.ai/functions/oracles/#synthetic-accessibility-sa) {cite:p}`huang:TDC:2021` (which uses RDKit internally).

## Prerequisites

None. This black box should run out-of-the-box.

## How to run

```python
import numpy as np
from poli.objective_repository import SAProblemFactory, SABlackBox

# Creating the black box
f = SABlackBox()

# Creating a problem
problem = SAProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input: (taken from the TDC)
x = np.array(["CCNC(=O)c1ccc(NC(=O)N2CC[C@H](C)[C@H](O)C2)c(C)c1"])

# Querying:
y = f(x)
print(y)  # Should be close to 2.85483733
```
