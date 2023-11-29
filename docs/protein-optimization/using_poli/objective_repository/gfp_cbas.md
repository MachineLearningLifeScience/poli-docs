# Protein Fluorescence (using `CBas`)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli protein_cbas](https://img.shields.io/badge/Environment-poli____protein-teal
)

[TODO: revise]

## About

This objective function returns the mean encoding (i.e. median brightness surrogate) using `CBas`.

## Prerequisites

- Assets: GFP dataframe, and model checkpoints as provided in the `poli` module

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In current environment

You will have to install the following dependencies:

```bash
pip install biopython python-levenshtein numpy pandas scipy torch torchvision torchaudio keras-core tensorflow
```

Then run

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# How to create
f, x0, y0 = objective_factory.create(
    name="gfp_cbas",
)

# Example input:
print(x0)

# Querying:
print(y0)  # The encoding of the first batch of GFP sequences
```

:::

:::{tab-item} In isolation

If you want us to handle dependencies, run

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# How to create
f, x0, y0 = objective_factory.create(
    name="gfp_cbas",
    wildtype_pdb_file=wildtype_pdb_file,
    force_register=True,
)

# Example input:
print(x0)

# Querying:
print(y0)  # The stability of your wildtype
```

```{warning}
Registering the objective function in this way will create a `conda` environment called `poli__protein_cbas` with the relevant dependencies.
```

:::

::::