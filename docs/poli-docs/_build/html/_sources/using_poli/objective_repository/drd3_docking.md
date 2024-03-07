# DRD3 docking (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli tdc](https://img.shields.io/badge/Environment-poli____tdc-teal
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

```python
import numpy as np
from poli.objective_repository import DRD3ProblemFactory, DRD3BlackBox

# Creating the black box
f = DRD3BlackBox()

# Creating a problem
problem = DRD3ProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input:
x = np.array(["c1ccccc1"])

# Querying:
y = f(x)
print(y)  # Should be close to -4.1
```
