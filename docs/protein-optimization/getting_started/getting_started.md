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

Right now, we only support two ways of installing `poli`: by cloning the repo and installing, or using `pip` and `git+`. [TODO: change from my fork to MLLS repo after merging]

::::{tab-set}

:::{tab-item} Installing using `pip +git`

If you are not interested in debugging, you can simply run

```bash
# in the poli-base env
pip install git+https://github.com/miguelgondu/poli.git
```

:::

:::{tab-item} Installing for debugging

If you are interested in debugging locally, clone and install as follows: 

```bash
# in the `poli-base` env.
$ git clone git@github.com:miguelgondu/poli.git
$ cd ./poli
$ pip install -e .
```

:::

::::

### Testing your installation

To make sure everything went well, you can test your `poli` installation by running

```bash
$ python -c "from poli.core.registry import get_problems ; print(get_problems())"
[]
```

If the installation isn't fresh/the only one in your system, you might actually get some registered problems.

## Running `poli` in Colab

With a little effort, you can run `poli` in Colab. [Check this example](https://colab.research.google.com/drive/1-IISCebWYfu0QhuCJ11wOag8aKOiPtls).


## Your first `poli` script

As you might have noticed, you can get a list of the registered problems using the `get_problems` method inside `poli.core.registry`. You can also get a list of objective functions available for installing/registration using `from poli.objective_repository import AVAILABLE_OBJECTIVES`:

```bash
$ python -c "from poli.objective_repository import AVAILABLE_OBJECTIVES ; print(AVAILABLE_OBJECTIVES)"
[..., 'white_noise']
```

Let's write a small script that installs `white_noise` from the repository:

```python
# see examples/minimal_working_example.py
from poli import objective_factory

problem_info, f, x0, y0, run_info = objective_factory.create(name="white_noise")

x = np.array([[1]])  # must be of shape [b, d], in this case [1, 1].
for _ in range(5):
    print(f"f(x) = {f(x)}")
```

If we run this script, `poli` will ask us to confirm that we want to register/install `"white_noise"` as an objective function (you can deactivate this confirmation step by passing the flag `force_register=True` to `.create`). Afterwards, it will print 5 evaluations of the objective function on the same input.


