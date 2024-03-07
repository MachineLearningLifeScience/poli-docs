# dockstring

![Type of objective function: discrete inputs](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli dockstring](https://img.shields.io/badge/Environment-poli____dockstring-teal
)

## About

[dockstring](https://github.com/dockstring/dockstring) is an objective function for ligand design (i.e. for finding a small molecule that docks well against a certain protein) {cite:p}`GarciaOrtegon:dockstring:2022`. It uses OpenBabel and rdkit to prepare the ligand, and AutoDock Vina for docking.

Since the score given by Vina is supposed to be minimized, our implementation returns the negative.

## Prerequisites

None! The implementation of [dockstring](https://github.com/dockstring/dockstring) comes with batteries included. You don't even have to set up Autodock Vina. Unfortunately, it will only work on MacOS and Linux.

## How to run

```python
import numpy as np
from poli.objective_repository import DockstringProblemFactory, DockstringBlackBox

# Creating the black box
f = DockstringBlackBox(target_name="DRD2")

# Creating a problem
problem = DockstringProblemFactory().create(target_name="DRD2")
f, x0 = problem.black_box, problem.x0

# Example input: risperidone
x = np.array(["CC1=C(C(=O)N2CCCCC2=N1)CCN3CCC(CC3)C4=NOC5=C4C=CC(=C5)F"])

# Querying:
y = f(x)
print(y)  # Should be 11.9
```

