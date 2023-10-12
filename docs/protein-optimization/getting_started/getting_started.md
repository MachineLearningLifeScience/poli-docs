# Getting started

In this chapter, we share with you how to install `poli`, and get started with registering objective functions.

## Installing locally

Unfortunately, we only support **Linux** and **MacOS** for now.

### Installing conda

`poli` is built on top of manipulating `conda` environments. It is therefore important for you to **install conda**. [Follow the documentation of Anaconda itself](https://conda.io/projects/conda/en/latest/user-guide/install/index.html).

Test that your installation went through by writing

```bash
$ conda --version
conda 23.7.2
```

It's okay if you have another version. Read more about [supported versions of `conda` (TODO:ADD)]().

### Installing `poli`

We recommend creating an environment called `poli-base`. **The only dependency `poli` has is `numpy`**:

```bash
$ conda create -n poli-base python=3.9
$ conda activate poli-base
$ pip install numpy
```

Right now, we only support two ways of installing `poli`: by cloning the repo and installing, or using `pip` and `git+`.

::::{tab-set}

:::{tab-item} Installing using `pip +git`

If you are not interested in debugging, you can simply run

```bash
# in the poli-base env
pip install git+https://github.com/MachineLearningLifeScience/poli.git@master
```

:::

:::{tab-item} Installing for debugging

If you are interested in debugging locally, clone and install as follows: 

```bash
# in the `poli-base` env.
$ git clone git@github.com:MachineLearningLifeScience/poli.git
$ cd ./poli
$ pip install -e .
```

A stable version can be found on the `master` branch, the bleeding-edge is on `dev`.

:::

::::

:::{warning}

`poli` works by creating shell scripts inside your home folder, under `./.poli_objectives`. Make sure you're okay with this.

:::

### Testing your installation

To make sure everything went well, you can test your `poli` installation by running

```bash
$ python -c "from poli.core.registry import get_problems ; print(get_problems())"
['aloha', 'white_noise']
```
In general: **all problems available will appear**. These two (`aloha` and `white_noise`) are available by default since their only requirements are `numpy` and `poli`. If the installation isn't fresh/the only one in your system, you might actually get more problems.

## Running `poli` on Colab

With a little effort, you can run `poli` on Colab. [Check this example](https://colab.research.google.com/drive/1-IISCebWYfu0QhuCJ11wOag8aKOiPtls).


## Your first `poli` script

As you might have noticed, you can get a list of the registered problems using the `get_problems` method inside `poli.core.registry`.

Let's write a small script that installs `white_noise` from the repository:

```python
# see poli/examples/minimal_working_example.py
import numpy as np
from poli import objective_factory

problem_info, f, x0, y0, run_info = objective_factory.create(name="white_noise")

x = np.array([["1", "2", "3"]])  # must be of shape [b, L], in this case [1, 3].
for _ in range(5):
    print(f"f(x) = {f(x)}")
```

If we run this script, it will print 5 evaluations of the objective function on the same input.

`white_noise` is a trivial example. We include plenty of examples on how to register objective functions that are more complex, including e.g. [computing the Quantitative Estimate of Druglikeness of a small molecule](../using_poli/objective_repository/rdkit_qed.md) or, if you have the `foldx` simulator installed, [how to compute the stability of a protein given a `.pdb` file](../using_poli/optimization_examples/protein-stability-foldx/optimizing_protein_stability.ipynb).

## Conclusion

This tutorial showed you how to install `poli`, and register `white_noise`, which is available inside `poli` itself.

The next chapters explain the basics of `poli`, such as registering your own objective functions, defining problem solvers in `poli-baselines`, and optimizing.
