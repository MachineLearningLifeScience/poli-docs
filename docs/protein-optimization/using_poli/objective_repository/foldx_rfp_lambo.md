# Protein (RFP) stability and SASA (using `foldx`,`lambo`)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli protein](https://img.shields.io/badge/Environment-poli____lambo
)

## About

This objective function returns stability using `foldx` and SASA, _exactly_ as done in the `lambo` implementation.

## Prerequisites

- Have `foldx` installed, and available in your home directory. We expect the following files to be there:
  - `~/foldx/foldx`: the binary. You might need to rename it.
  - `~/foldx/rotabase.txt`: a text file necessary for `foldx` to run.
- Have `lambo` checked out, preferrably in the home directory, specifically containing: 
  - `lambo.tasks.proxy_rfp.proxy_rfp.ProxyRFPTask`
  - the rfp data: see `~/lambo/assets/fpbase`

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In current environment

You will have to install the following two dependencies:

```bash
pip install -r ~/lambo/requirements.txt
```

This contains: `pytorch botorch python-levenshtein wandb biopython hydra-core pymoo pandas deepchem transformers selfies jupyter seaborn pyscreener` and other packages.

Then run

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
print(y0)  # The stability of your wildtype
```

You could also pass an `problem: ProblemSetupInformation` to the create method. For the alphabet reference by default, [we use this encoding](https://github.com/MachineLearningLifeScience/poli/blob/44cad2a5c95f209aeb24d4893d162b3359ca91a3/src/poli/core/util/proteins/defaults.py#L1).

:::

::::