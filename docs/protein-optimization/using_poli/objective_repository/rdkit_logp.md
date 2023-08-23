# Log-solubility (logP)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli chem](https://img.shields.io/badge/Environment-poli____chem-teal
)

## About

This objective function returns the Quantitative Estimate of Druglikeness (QED) using `RDKit`. During creation, you can specify whether you are measuring the QED of a SMILES string, or a SELFIES.

## Prerequisites

- An alphabet of tokens `{str: int}` as a json file. For example, in the case of SELFIES, this file would be
```json
# alphabet_selfies.json
{
    "": 0,       # an empty padding
    "[C]": 1,
    ...
}
```

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In current environment

You will have to install the following two dependencies:

```bash
pip install rdkit selfies
```

Then run

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# The path to your alphabet
path_to_alphabet = Path("path/to/alphabet_selfies.json")

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="rdkit_logp",
    path_to_alphabet=path_to_alphabet,
    string_representation="SELFIES"  # it is "SMILES" by default.
    )

# Example input: a single carbon
x = np.array([[1]])

# Querying:
print(f(x))  # Should be close to 0.35978
```

:::

:::{tab-item} In isolation

If you want us to handle dependencies, run

```python
from pathlib import Path

import numpy as np

from poli import objective_factory


# The path to your alphabet
path_to_alphabet = Path("path/to/alphabet_selfies.json")

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="rdkit_logp",
    path_to_alphabet=path_to_alphabet,
    string_representation="SELFIES"  # it is "SMILES" by default.
    force_register=True, 
)

# Example input: a single carbon
x = np.array([[1]])

# Querying:
print(f(x))  # Should be close to 0.6361
```

```{warning}
Registering the objective function in this way will create a `conda` environment called `poli__chem` with the relevant dependencies.
```

:::

::::
