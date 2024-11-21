# Getting started

In this chapter, we share with you how to install `poli` and `poli-baselines`, and get started with benchmarking black box functions.

## Installation

Unfortunately, we only support **Linux** and **MacOS** for now.

### (Optional) Installing conda

One of `poli`'s strengths comes from isolating black box functions. If you want to use this functionality, we encourage you to **install conda**. [Follow the documentation of Anaconda itself](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

Test that your installation went through by writing

```bash
$ conda --version
conda 23.11.0  # Yours might be different, and that's fine.
```

It's okay if you have another version. We have tested this documentation on the version showed.

### Installing `poli`

Right now, we only support two ways of installing `poli`: by cloning the repo and installing, or using `pip`.

::::{tab-set}

:::{tab-item} Installing using `pip`

You can install `poli` in an environment by running

```bash
pip install poli-core
```

This is the base installation of `poli`. If you want to use certain black boxes, you can install their dependencies by running e.g.
- `pip install poli-core[tdc]` to run the PMO benchmark.
- `pip install poli-core[ehrlich]` to run the EhrlichHolo black box.

and more. Check the documentation of each black box for more details.

You can install the bleeding edge version of `poli` using `git+`:

```bash
# in the poli-base env
pip install "poli-core @ git+https://github.com/MachineLearningLifeScience/poli.git@dev"
```

:::

:::{tab-item} Installing for debugging

If you are interested in debugging locally, clone and install as follows: 

```bash
git clone git@github.com:MachineLearningLifeScience/poli.git@dev
cd ./poli
pip install -e .
```

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
pip install "poli-baselines @ git+https://github.com/MachineLearningLifeScience/poli-baselines.git@main"
```

You can install the dependencies for specific solvers by replacing `poli-baselines` with e.g. `poli-baselines[ax]` for ax-related solvers, `poli-baselines[bounce]` for the Bounce solver, and so on. Check the documentation of each solver for more information.

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
$ python -c "import poli ; print(poli.__version__)"
1.1.0  # Might be different, that's fine.
```
All problems available will appear, but some of them will have more pre-requisites (e.g. installing `foldx` or having OpenBabel).

You should also be able to run
```bash
$ python -c "import poli_baselines ; print(poli_baselines.__version__)"
1.0.2.dev1  # Might be different, that's fine.
```

## Your first script using `poli`

Let's write a small script that creates an instance of `white_noise` from the repository:

```python
# see poli/examples/minimal_working_example.py
import numpy as np
from poli import objective_factory

problem = objective_factory.create(name="white_noise")
f, x0 = problem.black_box, problem.x0

x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].
for _ in range(5):
    print(f"f(x) = {f(x)}")
```

If we run this script, it will print 5 evaluations of the objective function on the same input.

## Other examples

`white_noise` is a trivial example. We include plenty of examples on how to register objective functions that are more complex, including e.g. [computing the Quantitative Estimate of Druglikeness of a small molecule](../using_poli/objective_repository/rdkit_qed.md) or, if you have the `foldx` simulator installed, [how to compute the stability of a protein given a `.pdb` file](../using_poli/optimization_examples/protein-stability-foldx/optimizing_protein_stability.ipynb).
