# Penalized logP (using `lambo`)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli lambo](https://img.shields.io/badge/Environment-poli____lambo-teal
)

## About

This objective function computes the penalized logP _exactly_ as is done in the `lambo` implementation[^1] {cite:p}`stanton2022accelerating`.

[^1]: If you check carefully, you might have noticed that they add to their implementation the empirical means and standard deviations of the ZINC dataset for the values they compute.

To do so, we import their scoring function.

## Prerequisites

### Python environment

We expect you to have [cloned and installed the `lambo` repository](https://github.com/samuelstanton/lambo). Since there are some files we can't install automatically using `pip install git+...`, we ask you to create a `conda` environment for the lambo tasks:

```
# From the root of the poli repository
conda env create --file src/poli/objective_repository/foldx_rfp_lambo/environment.yml
```

Activate the environment you just created using
```
conda activate poli__lambo
```

### `lambo`

We also need `lambo`'s tasks to be available in Python's path for `poli__lambo`:

```bash
# In the poli__lambo environment
git clone https://github.com/samuelstanton/lambo    # For reference, we use 431b052
cd lambo
pip install -e .  
```

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

You can only run this objective function either in the `poli__lambo`, or as an isolated process (which runs this environment underneath).

::::{tab-set}

:::{tab-item} (Isolated) in the `poli__lambo` environment

After the setup described above, you can simply run the following code from 

```python
import numpy as np

from poli import objective_factory

# Using create
f, x0, y0 = objective_factory.create(name="penalized_logp_lambo")

# An example input
print(x0)

# The example's output
print(y0)

# Terminating the isolated process (if it was created)
f.terminate()
```

:::

::::

### Other keyword arguments:

- `penalized: bool = True`. Whether we are evaluating penalized logP or not.
- `string_representation: str = "SMILES"`. Can be either `"SMILES"` or `"SELFIES"`.
