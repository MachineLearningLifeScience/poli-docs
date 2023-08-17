# Contributing a new problem to the repository

This tutorial covers how problems are structured in the repository, and what it takes to add a new one.

## The structure of a problem

If you take a look at the source code of `poli`, you will find a folder called `objective_repository`. This is where all the objective functions in the repository live. The structure of a generic problem goes as follows

```bash
poli/objective_repository
├── problem_name              # Has the name of the registered problem (exactly)
│   ├── environment.yml       # The env. where ./register.py and the problem will run
│   └── register.py           # Definition and registration of the problem
```

You can also have as many other files as you want. Think of the folder `.../problem_name` as a small project as of itself: you can have Python dependencies that will get appended to the path at runtime.

**For example:**, let's take a look at the problem folder of `super_mario_bros`

```bash
├── super_mario_bros
│   ├── environment.yml
│   ├── register.py
│   ├── example.pt           # < --
│   ├── level_utils.py       # < --
│   ├── model.py             # < --  extra files needed
│   ├── readme.md            # < --  for the simulation
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
from typing import Tuple

import numpy as np

from poli.core.abstract_black_box import AbstractBlackBox
from poli.core.abstract_problem_factory import AbstractProblemFactory
from poli.core.problem_setup_information import ProblemSetupInformation


class YourBlackBox(AbstractBlackBox):
    def __init__(self, L: int = np.inf):
        super().__init__(L=L)

    # The only method you have to define
    def _black_box(self, x: np.ndarray, context: dict = None) -> np.ndarray:
        return ...


class YourProblemFactory(AbstractProblemFactory):
    def get_setup_information(self) -> ProblemSetupInformation:
        # The tokens of your alphabet
        alphabet_symbols = [...]
        
        # The encoding
        alphabet = {symbol: i for i, symbol in enumerate(alphabet_symbols)}

        # A description of the problem
        # See more in the chapter about defining
        # problem factories.
        return ProblemSetupInformation(
            name="your_problem",         # HAS to be the same name as the parent folder.
            max_sequence_length=..., 
            aligned=...,
            alphabet=alphabet,
        )

    def create(self, seed: int = 0, keyword_1 = ..., keyword_2 = ...) -> Tuple[AbstractBlackBox, np.ndarray, np.ndarray]:
        # Manipulate keywords you might need at creation time...
        ...
        
        # The maximum length you defined above
        L = self.get_setup_information().get_max_sequence_length()
        
        # Creating your black box function
        f = YourBlackBox(L=L)
        
        # Your first input (an np.array)
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
It is important that name of your problem should be the name of the folder it's contained, exactly. (We advice using `camel_case`).
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
    - "git+https://github.com/miguelgondu/poli.git"
    - YOUR OTHER DEPENDENCIES
```

This environment will be created (if it doesn't exist yet), and will be used to run `register.py`.

:::{admonition} Why `conda`?
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
    - "git+https://github.com/miguelgondu/poli.git"

```

It installs an `openjdk` that will be added to the path when the environment is active. Moreover, you can also hack your way around installing conda and creating conda environments inside Colab.

:::

## Testing your installation

If you
1. have put your new problem is inside `poli/objective_repository`,
2. have a `register.py` that creates and register your problem factory,
3. have an `environment.yml` that describes the environment you use,

then you should be set!

You can test that your problem is registerable by creating a fresh environment that includes poli, and running

```bash
$ python -c "from poli.core.registry import get_problems; print(get_problems())"
[...]  # A list, without your problem in it.
```

Your problem is not registered yet, so don't fret. You can check _if_ you can register it by running

```bash
$ python -c "from poli.objective_repository import AVAILABLE_OBJECTIVES; print(AVAILABLE_OBJECTIVES)"
[..., "your_problem", ...]   # If all goes well, you should see "your_problem" here.
```

If you can find your problem in this list, then you're set! You should be able to run

```python
from poli import objective_factory

problem_info, f, x0, y0, _ = objective_factory.create(
    name="your_problem",
    ...,
    keyword_1=...,      # <-- Keywords you (maybe) needed
    keyword_2=...       # <-- at your_factory.create(...)
)
```

`poli` will ask you to confirm that you want to register your problem (you can force the registration by passing `force_register=True` to `objective_factory.create`).

## Submitting a pull request

If you want to share your problem with us, feel free to create a pull request in our repository: https://github.com/MachineLearningLifeScience/poli
