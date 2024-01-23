# Adding a new problem to the repository

This tutorial covers how problems are structured in the repository, and what it takes to add a new one.

## The structure of a problem

If you take a look at the source code of `poli`, you will find a folder called `objective_repository`. This is where all the objective functions in the repository live. The structure of a generic problem goes as follows

```bash
poli/objective_repository
├── problem_name              # Has the name of the registered problem (exactly)
│   ├── __init__.py           # Necessary, else it doesn't get included in the pip install.
│   ├── environment.yml       # The env. where ./register.py and the problem will run
│   └── register.py           # Definition and registration of the problem
```

You can also have as many other files as you want. Think of the folder `.../problem_name` as a small project as of itself: you can use any internal code you write here, since it'll be carried with `poli` at installation time.

**For example:** let's take a look at the problem folder of `super_mario_bros`

```bash
├── super_mario_bros
│   ├── __init__.py         
│   ├── environment.yml
│   ├── register.py
│   ├── example.pt           # < --
│   ├── level_utils.py       # < --
│   ├── model.py             # < --  extra files needed
│   ├── readme.md            # < --  for the black box
│   ├── simulator.jar        # < --  to run.
│   └── simulator.py         # < --
```

:::{warning}
As a general rule: **don't assume that your files will be there after `pip install git+...`**. File endings different from `.py` and `.yml` will be ignored by `pip` during installation. An alternative, then, is to download them in your `register.py`.
:::

## A generic `register.py`

The average `register.py` has the following structure

```python
# An average register.py
from typing import Tuple, List

import numpy as np

from poli.core.abstract_black_box import AbstractBlackBox
from poli.core.abstract_problem_factory import AbstractProblemFactory
from poli.core.problem_setup_information import ProblemSetupInformation

# Files that are in the same folder as
# register will get added to the
# PYTHONPATH at runtime.
# Imagining you have your_local_dependency.py
# in the same folder as register.py...
from your_local_dependency import ...


class YourBlackBox(AbstractBlackBox):
    def __init__(
        self,
        info: ProblemSetupInformation,
        your_arg: str,
        your_second_arg: List[float],
        your_kwarg: str=...,
        batch_size: int = None,
        parallelize: bool = False,
        num_workers: int = None,
        evaluation_budget: int = float("inf")
    ):
        super().__init__(
            info=info,
            batch_size=batch_size,
            parallelize=parallelize,
            num_workers=num_workers,
            evaluation_budget=evaluation_budget,
        )

        #... your manipulation of args and kwargs.

    # The only method you have to define
    def _black_box(self, x: np.ndarray, context: dict = None) -> np.ndarray:
        return ...


class YourProblemFactory(AbstractProblemFactory):
    def get_setup_information(self) -> ProblemSetupInformation:
        # Your alphabet
        alphabet = [...]

        # A description of the problem
        # See more in the chapter about defining
        # problem factories.
        return ProblemSetupInformation(
            name="your_problem",         # HAS to be the same name as the parent folder.
            max_sequence_length=..., 
            aligned=...,
            alphabet=alphabet,
        )

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
    ) -> Tuple[AbstractBlackBox, np.ndarray, np.ndarray]:
        # Manipulate args and kwargs you might need at creation time...
        ...
        
        # Getting the problem information
        problem_info = self.get_setup_information()
        
        # Creating your black box function
        f = YourBlackBox(
            info=problem_info,
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

        return f, x0, f(x0)


if __name__ == "__main__":
    from poli.core.registry import register_problem

    # Once we have created a simple conda enviroment
    # (see the environment.yml file in this folder),
    # we can register our problem s.t. it uses
    # said conda environment.
    your_problem_factory = YourProblemFactory()
    register_problem(
        your_problem_factory,                   
        conda_environment_name="your_env",    # This is the env specified
                                              # by your environment.yml
    )

```

That is, **the script creates and registers** your problem factory.

:::{warning}
It is important that name of your problem should be the name of the folder it's contained, **exactly**. (We advice using `camel_case`).
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

This environment will be created (if it doesn't exist yet), and will be used to run `register.py`.

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

## Testing your installation

If you
1. have put your new problem is inside `poli/objective_repository`,
2. have a `register.py` that creates and register your problem factory,
3. have an `environment.yml` that describes the environment you use,

then you should be set!

You can test that your problem is registerable by running

```bash
$ python -c "from poli.core.registry import get_problems; print(get_problems())"
[..., "your_problem", ...]  # A list with your problem in it
```

If you can find your problem in this list, then you're set! You should be able to run

```python
from poli import objective_factory

problem_info, f, x0, y0, _ = objective_factory.create(
    name="your_problem",
    ...,
    your_arg_1=...,      # <-- Keywords you (maybe) needed
    your_arg_2=...,       # <-- at your_factory.create(...)
    your_kwarg=...,       # <--
                            # For now, only certain types are
                            # supported: str, int, bool, float,
                            # None, and lists thereof.
)
```

## (Optional) Making your problem be available if dependencies are met

At this point, you can run your objective function in an isolated process (which will literally import the factory and the black box function from the `register.py` you wrote).

A better alternative is to get direct access to the object itself. Having access to the actual class makes your life easy, especially when it comes to using debugging tools like the ones in VSCode.

If you want to make your problem available if it can be imported, take a look at `src/poli/objective_repository/__init__.py`. Add a block like this one at the end of it:

```python
#... the rest of poli/objective_repository/__init__.py

# A block you could add:
try:
    from .your_problem.register import YourProblemFactory

    AVAILABLE_PROBLEM_FACTORIES["your_problem"] = YourProblemFactory
except ImportError:  # Maybe you'll need to check for other errors.
    pass

```

`AVAILABLE_PROBLEM_FACTORIES` is keeping track of all the problem factories we can import without needing to isolate the process. If a problem is in this dict, it will appear when querying `get_problems()`, and it will be passed at `objective_factory.create` time.


## Submitting a pull request

If you want to share your problem with us, feel free to create a pull request in our repository following the instructions in our `CONTRIBUTING.md`: https://github.com/MachineLearningLifeScience/poli
