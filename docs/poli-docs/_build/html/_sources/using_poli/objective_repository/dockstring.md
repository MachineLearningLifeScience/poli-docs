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


## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] García-Ortegón, Miguel, Gregor N. C. Simm, Austin J. Tripp, José Miguel Hernández-Lobato, Andreas Bender, and Sergio Bacallado. “DOCKSTRING: Easy Molecular Docking Yields Better Benchmarks for Ligand Design.” Journal of Chemical Information and Modeling 62, no. 15 (August 8, 2022): 3486–3502. https://doi.org/10.1021/acs.jcim.1c01334.


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{GarciaOrtegon:dockstring:2022,
  title    = {DOCKSTRING: Easy Molecular Docking Yields Better Benchmarks for Ligand Design},
  volume   = {62},
  issn     = {1549-9596, 1549-960X},
  doi      = {10.1021/acs.jcim.1c01334},
  number   = {15},
  journal  = {Journal of Chemical Information and Modeling},
  author   = {García-Ortegón, Miguel and Simm, Gregor N. C. and Tripp, Austin J. and Hernández-Lobato, José Miguel and Bender, Andreas and Bacallado, Sergio},
  year     = {2022},
  month    = aug,
  pages    = {3486–3502},
  language = {en}
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
