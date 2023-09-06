# DRD3 docking (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli lambo](https://img.shields.io/badge/Environment-poli____lambo-teal
)

## About

This objective function computes the docking score of a small molecule w.r.t. the protein `3pbl`, [which is the canonical example in the Therapeutics Data Common's docking oracles](https://tdcommons.ai/functions/oracles/#docking-scores) {cite:p}`huang:TDC:2021`. Under the hood, it uses pyscreener, vina and the ADFR suite.

## Prerequisites

### Installing AutoDock Vina

#### Download the files

[Download AutoDock Vina from the Center for Computational Structural Biology's website](https://vina.scripps.edu/downloads/). Uncompress them.

#### Add the binary folder to the path.

Add this to the path by including `export PATH=path/to/AutoDock_vina/bin:$PATH` in your `~/.bashrc` or `~/.zshrc`.

```bash
# In your ~/.bashrc or ~/.zshrc
export PATH=path/to/AutoDock_vina/bin:$PATH
```

### Installing the ADFR suite

#### Download the files

[Download the installable files](https://ccsb.scripps.edu/adfr/downloads/). It's likely that you will have to run the `./install.sh` script inside the folder, and thus you might have to change its permissions for execution using `chmod +x`

#### Install it

After running `./install.sh`, you should be able to find `.../bin/prepare_receptor`.

#### Add `prepare_receptor` to the path

For the docking to run, `pyscreener` needs access to the `prepare_receptor` binary. However, adding all of the ADFR `bin` folder is sometimes problematic, since it has a version of Python inside.

Thus, we recommend creating a symlink. Write this in your `~/.bashrc` or `~/.zshrc`:

```bash
# In your ~/.bashrc or ~/.zshrc
ln -sf /path/to/ADFR/bin/prepare_receptor /path/to/AutoDock_vina/bin
```

### Create the `poli__lambo` environment

#### Create the environment from the yml file

This can easily be done by running

```bash
# From the base of the poli repo
conda env create --file src/poli/objective_repository/drd3_docking/environment.yml
```

This particular example _doesn't_ need to have the `lambo` package installed.

### Making sure you're all set

If the set-up above was successful, you should be able to run

```bash
which vina
# /path/to/your/bin/vina
```

and

```bash
which prepare_receptor
# /path/to/your/bin/prepare_receptor
```

## How to run

You can only run this objective function either in the `poli__lambo` environment, or as an isolated process (which runs this environment underneath).

:::{warning}
Running this objective function will create an `./oracle` folder on your working directory, where it will download the relevant `.pdb` files.
:::

::::{tab-set}

:::{tab-item} (Isolated) in the `poli__lambo` environment

After the setup described above, you can simply run the following code from 

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# How to create
problem_info, f, x0, y0, run_info = objective_factory.create(
    name="drd3_docking",
    force_register=True
)

# Example input:
print(x0)  # [['c' '1' 'c' 'c' 'c' 'c' 'c' '1']]

# Querying:
print(y0)  # [[-4.1]]
```

:::

::::

<!-- ## References

:::{bibliography}
:style: alpha

::: -->