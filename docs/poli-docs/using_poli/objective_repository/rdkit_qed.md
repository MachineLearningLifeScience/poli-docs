# Quantitative Estimate of Druglikeness (QED)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli chem](https://img.shields.io/badge/Environment-poli____chem-teal
)

## About

This objective function returns the Quantitative Estimate of Druglikeness (QED) using `RDKit` {cite:p}`rdkit`. You can specify whether you are measuring the QED of a SMILES string, or a SELFIES.

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

## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] RDKit community. (2006). RDKit: Open-source cheminformatics. GitHub. Available at: https://github.com/rdkit/rdkit. Accessed on 12th of April, 2024.


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```
@misc{rdkit,
  author = {RDKit},
  title = {RDKit: Open-source cheminformatics},
  year = {2006},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/rdkit/rdkit}}
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