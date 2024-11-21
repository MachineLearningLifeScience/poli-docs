# Adding a new black box to the repository

This tutorial covers how black boxes and problems are structured in the repository, and what it takes to add a new one.

If you want to implement your own black box and problem, we recommend copy-pasting an existing folder (e.g. `dockstring`), and modifying it to suit your needs. We provide a checklist at the end of this tutorial for the things you need to pay attention to.

## The structure of a problem

If you take a look at the source code of `poli`, you will find a folder called `objective_repository`. This is where all the objective functions in the repository live. The structure of a generic problem goes as follows

```bash
poli/objective_repository
├── my_problem_name
│   ├── __init__.py  # Necessary, so that it gets installed with pip.
│   ├── information.py # A BlackBoxInformation containing a desc. of the black box
│   ├── isolated_function.py  # The logic of your black box, as complex as you want.
│   ├── environment.yml  # The conda env where isolated_function.py runs
│   └── register.py  # Boilerplate. the problem factory and black box interface.
```

You can also have as many other files as you want. Think of the folder `.../problem_name` as a small project as of itself: you can use any internal code you write here, since it'll be carried with `poli` at installation time.

**For example:** let's take a look at the problem folder of `super_mario_bros`

```bash
├── super_mario_bros
│   ├── __init__.py
│   ├── environment.yml
│   ├── information.py
│   ├── isolated_function.py
│   ├── register.py
│   ├── requirements.txt
│   ├── example.pt  #    <--
│   ├── level_utils.py # <--
│   ├── model.py  #      <-- Extra files needed
│   ├── simulator.jar  # <-- to run the black box.
│   └── simulator.py  #  <--
```

:::{warning}
As a general rule: **don't assume that your files will be there after `pip install git+...`**. File endings different from `.py` and `.yml` will be ignored by `pip` during installation. An alternative, then, is to download them in your `isolated_function.py` or `register.py`.
:::

## Specifying your problem information in `information.py`

We recommend you create a script called `information.py`, and write your black box's information in it:

```python
# my_problem_name/information.py

from poli.core.black_box_information import BlackBoxInformation

my_problem_information = BlackBoxInformation(
    name="my_problem_name",           # HAS to be the same name as the folder.
    max_sequence_length=2,            # Maximum sequence length (usually np.inf)
    aligned=True,                     # Whether sequences are aligned.
    fixed_length=True,                # Whether sequences have fixed length.
    deterministic=False,              # Whether the problem is deterministic
    alphabet=None,                    # A potential alphabet of accepted tokens
    log_transform_recommended=True,   # Whether the output should be log-transformed
    discrete=False,                   # Discrete inputs
    padding_token="",               # A token that could be used for padding
)

```

## A generic `isolated_function.py`

Think of `isolated_function.py` as the entry-route to all the complex, dependency-heavy logic of your black box.

We expect you to implement a subclass of an `AbstractIsolatedFunction`. These are dynamically instanced in isolated environments, such as the one you provide in `environment.yml`. 

The average structure of this file would be as follows:

```python
# my_problem_name/isolated_function.py,
# able to run inside the conda env you specify in environment.yml

# Importing whatever you need for the implementation of the black box.
import one_dependency
import another_dependency
from yet_another_dependency import ComplicatedClass

# Importing the abstract isolated function
from poli.core.abstract_isolated_function import AbstractIsolatedFunction

# Your implementation of the isolated logic
# You can have an __init__ if you want!
class MyIsolatedLogic(AbstractIsolatedFunction):
    def __call__(self, x: np.ndarray, context=None) -> np.ndarray:
        """
        Your implementation of the black box function.
        """
        ...

        return y

if __name__ == "__main__":
    from poli.core.registry import register_isolated_function

    register_isolated_function(
        MyIsolatedLogic,  # Your function, designed to be isolated
        name="my_problem_name__isolated",  #  Same name as the problem and folder, ending on __isolated.
        conda_environment_name="conda_env_inside_environment_file",  # The name of the conda env inside environment.yml.
    )
```

When run, this script will **register** your isolated logic. By this, we mean creating a shell script inside `~/.poli_objectives` that spawns an isolated process with which we communicate when you query new points.


:::{warning}
It is important that name of your isolated function is exactly the name of the folder it's contained in, followed by `__isolated`. (We advice using `camel_case`).
:::

## A generic `register.py`

The average `register.py` has the following structure

```python
# my_problem_name/register.py
# This one NEEDS TO run on a conda env. with minimal dependencies (numpy)
from typing import Tuple, List

import numpy as np

from poli.core.abstract_black_box import AbstractBlackBox
from poli.core.abstract_problem_factory import AbstractProblemFactory
from poli.core.black_box_information import BlackBoxInformation
from poli.core.problem import Problem

from poli.core.util.isolation.instancing import instance_function_as_isolated_process

from poli.objective_repository.my_problem_name.information import my_problem_info


class MyBlackBox(AbstractBlackBox):
    def __init__(
        self,
        your_arg: str,
        your_second_arg: List[float],
        your_kwarg: str=...,
        batch_size: int = None,
        parallelize: bool = False,
        num_workers: int = None,
        evaluation_budget: int = float("inf"),
        force_isolation: bool = False,
    ):
        super().__init__(
            batch_size=batch_size,
            parallelize=parallelize,
            num_workers=num_workers,
            evaluation_budget=evaluation_budget,
            force_isolation=force_isolation,
        )

        #... your manipulation of args and kwargs.

        # Importing the isolated logic if we can:
        _ = get_inner_function(
            isolated_function_name="your_problem__isolated",  # <-- modify this
            class_name="MyIsolatedLogic",  # <-- modify this
            module_to_import="poli.objective_repository.your_problem.isolated_function",  # <-- modify this
            force_isolation=force_isolation,
            **other_kwargs_that_go_into_MyIsolatedLogic  # <-- modify this
        )

    # Boilerplate for the black box call:
    def _black_box(self, x: np.ndarray, context: dict = None) -> np.ndarray:
        inner_function = get_inner_function(
            isolated_function_name="your_problem__isolated",  # <-- modify this
            class_name="MyIsolatedLogic",  # <-- modify this
            module_to_import="poli.objective_repository.your_problem.isolated_function",  # <-- modify this
            force_isolation=force_isolation,
            **other_kwargs_that_go_into_MyIsolatedLogic  # <-- modify this
        )
        return inner_function(x, context)

    # A static method that gives you access to the information.
    @staticmethod
    def get_black_box_info() -> BlackBoxInformation:
        return my_problem_info

class MyProblemFactory(AbstractProblemFactory):
    def get_setup_information(self) -> BlackBoxInformation:
        return my_problem_info

    def create(
        self,
        seed: int = None,
        your_arg: str = ...,
        your_second_arg: List[float] = ...,
        your_kwarg: str = ...,
        batch_size: int = None,
        parallelize: bool = False,
        num_workers: int = None,
        evaluation_budget: int = float("inf"),
        your_second_arg: List[float] = ...,
    ) -> Problem:
        # Manipulate args and kwargs you might need at creation time...
        ...
        
        # Creating your black box function
        f = MyBlackBox(
            your_arg=your_arg,
            your_second_arg=your_second_arg,
            your_kwarg=your_kwarg,
            batch_size=batch_size,
            parallelize=parallelize,
            num_workers=num_workers,
            evaluation_budget=evaluation_budget,
        )
        
        # Your first input (an np.array[str] of shape [b, L] or [b,])
        x0 = ...

        return Problem(f, x0)
```

That is, **the script provides an access to your isolated logic**. Now users can create a new problem factory or black box without having to worry about having the right dependencies.

:::{warning}
It is important that name of your problem should be the name of the folder it's contained in, **exactly**. (We advice using `camel_case`).
:::

:::{warning}

`poli` is under active development. The input kwargs to the abstract black box
and to the create method are under active development. Your IDE should
tell you automatically, though!

:::

## A generic `environment.yml`

You will usually develop your black-box objective function inside an environment, say `your_env`. You need to specify all these requirements in the `environment.yml`, generically:

```yml
name: your_env
channels:
  - defaults
dependencies:
  - python=3.9
  - pip
  - pip:
    - numpy
    - "git+https://github.com/MachineLearningLifeScience/poli.git@dev"
    - YOUR OTHER DEPENDENCIES
```

This environment will be created (if it doesn't exist yet), and will be used to run `isolated_function.py`.

:::{admonition} Why `conda`?
:class: dropdown

Conda environments can be quite good! For example, the `super_mario_bros` environment contains a Java runtime. This is the `environment.yml` for said problem:

```yml
name: poli__mario
channels:
  - defaults
  - conda-forge
  - pytorch
dependencies:
  - python=3.9
  - conda-forge::openjdk
  - cpuonly
  - pytorch
  - pip
  - pip:
    - numpy
    - click
    - "git+https://github.com/MachineLearningLifeScience/poli.git@dev"

```

It installs an `openjdk` that will be added to the path when the environment is active. Moreover, [`conda` is also installable in Google Colab, allowing you to use `poli` there](https://colab.research.google.com/drive/1-IISCebWYfu0QhuCJ11wOag8aKOiPtls?usp=sharing).

:::

## Adding your new black box to the repository's `__init__`

Once you do this, you can add an import to `poli/objective_repository/__init__.py`:

```python
# Add something like this after other imports
from .my_problem_name.register import MyBlackBox, MyProblemFactory


# Add your problem to the available problem factories and black boxes

AVAILABLE_PROBLEM_FACTORIES = {
    ...,
    "my_problem_name": MyProblemFactory,  # <-- add this
    ...
}

AVAILABLE_BLACK_BOXES = {
    ...,
    "my_problem_name": MyBlackBox,  # <-- add this
    ...
}


```

## Testing your installation

If you
1. have put your new problem is inside `poli/objective_repository`,
2. have an `information.py` that describes your black box,
3. have an `isolated_function.py` that implements the complex logic of your black box and registers it,
4. have a `register.py` that creates your problem factory and black box,
5. have an `environment.yml` that describes the environment you use,
6. have imported your black box and factory in `objective_repository/__init__.py`,

then you should be set!

To test, you can run

```python
from poli import objective_factory

problem = objective_factory.create(
    name="your_problem",
    ...,
    your_arg_1=...,      # <-- Keywords you (maybe) needed
    your_arg_2=...,       # <-- at your_factory.create(...)
)
```

or you could just import your black box as
```python
from poli.objective_repository import MyBlackBox

f = MyBlackBox(...)
```

## Submitting a pull request

If you want to share your problem with us, feel free to create a pull request in our repository following the instructions in our `CONTRIBUTING.md`: https://github.com/MachineLearningLifeScience/poli
