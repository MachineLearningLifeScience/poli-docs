# Protein (RFP) stability and SASA (using `foldx`,`lambo`)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli protein](https://img.shields.io/badge/Environment-poli____lambo-teal)

## About

This objective function returns stability using `foldx` and SASA, _exactly_ as done in the `lambo` implementation.

## Prerequisites

### `foldx`

We need you to have `foldx` installed, and available in your home directory. We expect the following files to be there:
  - `~/foldx/foldx`: the binary. You might need to rename it.
  - `~/foldx/rotabase.txt`: a text file necessary for `foldx` to run.

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

In particular, we need
- `lambo.tasks.proxy_rfp.proxy_rfp.ProxyRFPTask`
- the rfp data: see `~/lambo/assets/fpbase`

Make sure the data is avaliable.

## How to run

You can only run this objective function either in the `poli__lambo` environment, or as an isolated process (which runs this environment underneath).

::::{tab-set}

:::{tab-item} (Isolated) in the `poli__lambo` environment

After the setup described above, you can simply run the following code from 

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="foldx_rfp",
)

# Example input:
print(x0)

# Querying:
print(y0)  # [[-11189.00587946    -39.8155    ], ...]
```

You could also pass an `problem: ProblemSetupInformation` to the create method. For the alphabet reference by default, [we use this encoding](https://github.com/MachineLearningLifeScience/poli/blob/44cad2a5c95f209aeb24d4893d162b3359ca91a3/src/poli/core/util/proteins/defaults.py#L1).

:::

::::