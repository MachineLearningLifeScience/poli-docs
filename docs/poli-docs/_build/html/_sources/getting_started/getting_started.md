# Getting started

In this chapter, we share with you how to install `poli`, and get started with calling and registering objective functions.

## Installation

Unfortunately, we only support **Linux** and **MacOS** for now.

### Installing conda

`poli` is built on top of manipulating `conda` environments. It is therefore important for you to **install conda**. [Follow the documentation of Anaconda itself](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

Test that your installation went through by writing

```bash
$ conda --version
conda 23.11.0  # Yours might be different, and that's fine.
```

It's okay if you have another version. We have tested this documentation on the version showed.

### Installing `poli`

We recommend creating an environment called `poli-base`.

```bash
$ conda create -n poli-base python=3.9
$ conda activate poli-base
```

Right now, we only support two ways of installing `poli`: by cloning the repo and installing, or using `pip` and `git+`.

::::{tab-set}

:::{tab-item} Installing using `pip git+`

If you are not interested in debugging, you can simply run

```bash
# in the poli-base env
pip install git+https://github.com/MachineLearningLifeScience/poli.git@dev
```

`dev` contains the bleeding-edge version, while `master` contains a stable release.

:::

:::{tab-item} Installing for debugging

If you are interested in debugging locally, clone and install as follows: 

```bash
# in the `poli-base` env.
$ git clone git@github.com:MachineLearningLifeScience/poli.git@dev
$ cd ./poli
$ pip install -e .
```

A stable version can be found on the `master` branch, the bleeding-edge is on `dev`.

:::

::::

:::{warning}

`poli` works by creating shell scripts inside your home folder, under `./.poli_objectives`. Make sure you're okay with this.

:::

### Installing `poli-baselines`

:::{warning}

`poli-baselines` is on alpha phase, and the API might change in the short future.

:::

::::{tab-set}

:::{tab-item} Installing using `pip git+`

If you are not interested in debugging, you can simply run

```bash
# in the poli-base env
pip install git+https://github.com/MachineLearningLifeScience/poli-baselines.git@main
```

:::

:::{tab-item} Installing for debugging

If you are interested in debugging locally, clone and install as follows: 

```bash
# in the `poli-base` env.
$ git clone git@github.com:MachineLearningLifeScience/poli-baselines.git@main
$ cd ./poli-baselines
$ pip install -e .
```

:::

::::

### Testing your installation

To make sure everything went well, you can test your `poli` installation by running

```bash
$ python -c "from poli import get_problems ; print(get_problems())"
['aloha', 'dockstring', ...]
```
All problems available will appear, but some of them will have more pre-requisites (e.g. installing `foldx` or having OpenBabel).

You should also be able to run
```bash
$ python -c "import poli_baselines ; print('All good!')"
```

## Your first script using `poli`

Let's write a small script that creates an instance of `white_noise` from the repository:

```python
# see poli/examples/minimal_working_example.py
import numpy as np
from poli import objective_factory

f, x0, y0 = objective_factory.create(name="white_noise")

x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].
for _ in range(5):
    print(f"f(x) = {f(x)}")
```

If we run this script, it will print 5 evaluations of the objective function on the same input.

`white_noise` is a trivial example. We include plenty of examples on how to register objective functions that are more complex, including e.g. [computing the Quantitative Estimate of Druglikeness of a small molecule](../using_poli/objective_repository/rdkit_qed.md) or, if you have the `foldx` simulator installed, [how to compute the stability of a protein given a `.pdb` file](../using_poli/optimization_examples/protein-stability-foldx/optimizing_protein_stability.ipynb).
