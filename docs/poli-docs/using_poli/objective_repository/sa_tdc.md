# Synthetic Accessibility (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli lambo](https://img.shields.io/badge/Environment-poli____lambo-teal
)

## About

This objective function computes the synthetic accesibility of a small molecule using [the Therapeutics Data Common's oracle](https://tdcommons.ai/functions/oracles/#synthetic-accessibility-sa) {cite:p}`huang:TDC:2021` (which uses RDKit internally).

## Prerequisites

## How to run

You can only run this objective function either in the `poli__tdc` environment, or as an isolated process (which runs this environment underneath).

:::{warning}
Running this objective function will create an `./oracle` folder on your working directory, where it will download the relevant files for the oracle to work.
:::

::::{tab-set}

:::{tab-item} (Isolated) in the `poli__tdc` environment

After the setup described above, you can simply run the following code from 

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# How to create
f, x0, y0 = objective_factory.create(
    name="sa_tdc",
    force_register=True
)

# Example input:
print(x0)  # [['C' 'C' 'N' 'C' ...]]

# Querying:
print(y0)  # [[2.8548]]
```

:::

::::
