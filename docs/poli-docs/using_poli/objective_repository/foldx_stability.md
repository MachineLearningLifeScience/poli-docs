# Protein stability (using `foldx`)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli protein](https://img.shields.io/badge/Environment-poli____protein-teal)

## About

This objective function returns the stability (i.e. negative energy) using `foldx`.

:::{note}

If you are interested in computing both a protein's stability and it's SASA score, try `foldx_stability_and_sasa` instead! Just change the `name` in the `create` method below.

:::

## Prerequisites

- Have `foldx` installed, and available in your home directory. We expect the following files to be there:
  - `~/foldx/foldx`: the binary. You might need to rename it.
  - `~/foldx/rotabase.txt`: a text file necessary for `foldx` to run (only if you are using v4 of `foldx`).
- A `wildtype_pdb_file`: a (repaired) pdb file of the wildtype.

:::{admonition} We can repair the file for you
:class: dropdown

By default, we will assume you are passing a repaired `pdb` file to us (indeed, we check if the filename contains `_Repair`). If you want us to repair the file for you and keep it in a cache, you can add the `eager_repair=True` keyword argument to the `create` method.

Otherwise, pre-repair your files using e.g.

```bash
~/foldx/foldx --command=RepairPDB --pdb your_file.pdb --water -CRYSTAL --pH 7.0
```

In our repairing process, we also remove heteroatoms using [`pdbtools`](https://www.bonvinlab.org/pdb-tools/).

:::

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In current environment

You will have to install the following two dependencies:

```bash
pip install biopython python-levenshtein pdb-tools
```

Then run

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# The path to your wildtype pdb
wildtype_pdb_file = Path("path/to/wildtype.pdb")

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="foldx_stability",
    wildtype_pdb_file=wildtype_pdb_file
)

# Example input: (an array of strings)
print(x0)

# Querying:
print(y0)  # The stability of your wildtype
```

:::

:::{tab-item} In isolation

If you want us to handle dependencies, run

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# The path to your wildtype pdb
wildtype_pdb_file = Path("path/to/wildtype.pdb")

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="foldx_stability",
    wildtype_pdb_file=wildtype_pdb_file,
    force_register=True,
)

# Example input:
print(x0)

# Querying:
print(y0)  # The stability of your wildtype

# Terminate the process.
f.terminate()
```

```{warning}
Registering the objective function in this way will create a `conda` environment called `poli__protein` with the relevant dependencies.
```

:::

::::

You could also pass an `alphabet: List[str]` to the create method. By default, [we use this encoding](https://github.com/MachineLearningLifeScience/poli/blob/44cad2a5c95f209aeb24d4893d162b3359ca91a3/src/poli/core/util/proteins/defaults.py#L1).
