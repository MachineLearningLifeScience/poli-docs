# Registering an objective function in poli

With `poli`, you can define and register black box objective functions. This page shows you how. For the entire script, check [`registering_aloha.py`](https://github.com/MachineLearningLifeScience/poli/blob/master/examples/a_simple_objective_function_registration/registering_aloha.py) in the examples of `poli`.

## An example of a discrete black box function

First, you need to define your black box function (inheriting from `AbstractBlackBox`).

As a basic example, consider the problem of searching sequences of length $L=5$ for the particular sequence "ALOHA". We can define the following objective function:

$$ f(5\text{-letter word}) = \#\text{of letters that match with ALOHA} $$

Two examples of how this function would evaluate:

$$ f(\text{ALOOF}) = 3, \text{ because of A, L, and O.}$$

$$ f(\text{FLEAS}) = 1, \text{ because of L.} $$

We can define and register this function into `poli` as follows:

## Defining black-box functions in poli

`poli` implements an abstract class for black box functions, and you only need to inherit from it. The syntax goes like this:

```python
# registering_aloha.py
import numpy as np

from poli.core.abstract_black_box import AbstractBlackBox
from poli.core.problem_setup_information import ProblemSetupInformation

# L stands for sequence length.
class OurAlohaBlackBox(AbstractBlackBox):
    def __init__(self, info: ProblemSetupInformation, batch_size: int = None):
        super().__init__(info, batch_size)

    # The only method you have to define
    def _black_box(self, x: np.ndarray, context: dict = None) -> np.ndarray:
        matches = x == np.array(["A", "L", "O", "H", "A"])
        return np.sum(matches, axis=1, keepdims=True)

```

As the code says, the only method you need to define is `_black_box(x: np.ndarray, context: dict = None)`, returning a numpy array of size `[b, 1]`. `AbstractBlackBox` takes it from there, making sure that the length of the inputs is correct and matches the maximum length specified in `info.get_max_sequence_length()`.

Black-box functions are inside **problems**. A problem contains not only a black-box objective function, but also the relevant information for the discrete problem: the alphabet, maximum sequence length, whether the sequences are aligned... This next section discusses how to define problem factories, which create instances of the problem.

## Defining problem factories

The class `AbstractProblemFactory` has two abstract methods you are expected to overwrite:
- `get_setup_information`, which returns a class of information including the name of the problem, the alphabet, and a couple more descriptors.
- `create`, which returns the black-box function `f`, the initial design `x_0`, and its evaluation `f(x_0)`

Let's build a problem factory for the `AlohaBlackBox`:

```python
# registering_aloha.py
from typing import Tuple
from string import ascii_uppercase

import numpy as np

from poli.core.abstract_black_box import AbstractBlackBox
from poli.core.abstract_problem_factory import AbstractProblemFactory
from poli.core.problem_setup_information import ProblemSetupInformation

class OurAlohaBlackBox(AbstractBlackBox):
    # the implementation discussed above
    ...

class OurAlohaProblemFactory(AbstractProblemFactory):
    def get_setup_information(self) -> ProblemSetupInformation:
        # The alphabet: ["A", "B", "C", ...]
        alphabet = list(ascii_uppercase)

        return ProblemSetupInformation(
            name="our_aloha",
            max_sequence_length=5,
            aligned=True,
            alphabet=alphabet,
        )

    # Adding **kwargs is necessary, since several things usually
    # get passed to the create method at initialization.
    def create(
        self, seed: int = None, **kwargs
    ) -> Tuple[AbstractBlackBox, np.ndarray, np.ndarray]:
        problem_info = self.get_setup_information()
        f = OurAlohaBlackBox(info=problem_info)
        x0 = np.array([["A", "L", "O", "O", "F"]])

        return f, x0, f(x0)
```

**and that's it!** Once you have defined your problem factory, you need to register it to be able to call it on-the-go.

:::{note}
The exact implementation of the `aloha` problem is slightly different: we allow users to e.g. query both integers or strings. Integers are interpreted as the token ids according to the alphabet.

Check the exact implementation on [`poli/objective_repository/aloha/register.py`](https://github.com/MachineLearningLifeScience/poli/blob/master/src/poli/objective_repository/aloha/register.py).
:::

## Registering the problem factory

### Creating a conda environment for your problem

First step is always **creating a conda environment for your problem**. In this case, we could do with just the base enviroment. However, for completion in the presentation, we will create a conda enviroment called `poli_aloha`. This is the enviroment description (which can be found under `environment.yml` in the examples folder for `aloha`):

```yml
# environment.yml
name: poli_aloha_problem
channels:
  - defaults
dependencies:
  - python=3.9
  - pip
  - pip:
    - numpy
    - "git+https://github.com/MachineLearningLifeScience/poli.git@master"
```

:::{admonition} Why conda? Why an entire environment?
:class: dropdown

Using `conda` allows us to package more than Python dependencies. In some examples you might see yourself needing to using e.g. a Java runtime. With `conda`, we can create environments that *include* these dependencies.

For an example, [check the script that registers *Super Mario Bros* as a problem factory](https://github.com/MachineLearningLifeScience/poli/blob/master/src/poli/objective_repository/super_mario_bros/register.py).

:::

Remember that you can create this environment by running

```bash
conda env create --file environment.yml
```

### Registering the problem factory in poli's registry

The problem factory can be registered using `register_problem`, from `poli.core.registry`:

```python
# registering_aloha.py

...

if __name__ == "__main__":
    from poli.core.registry import register_problem

    # Once we have created a simple conda enviroment
    # (see the environment.yml file in this folder),
    # we can register our problem s.t. it uses
    # said conda environment.
    aloha_problem_factory = OurAlohaProblemFactory()
    register_problem(
        aloha_problem_factory,
        conda_environment_name="poli_aloha_problem",
    )
```

**And you're good!** After this, you should be able to call the aloha problem somewhere else, and even using a *different* conda environment from `poli_aloha_problem` if you so want.

:::{admonition} Need to add more python dependencies/paths?
:class: dropdown

`register_problem` also takes `python_paths: List[str]`, allowing you to add more dependencies to the Python path before running the black box function.

:::

:::{admonition} Where is this problem registered?

`poli` registers this objective as a shell file `.sh` inside `~/.poli_objectives`.

As you can check, this script runs `poli/objective.py` inside the conda environment you specified on registration. `objective.py` is the main workhorse of `poli`: it starts a process in which the objective function waits for next inputs.

:::

## Calling the registered problem

To check that we can indeed call the problem from somewhere else, let's write a second file called `querying_aloha.py` where we instantiate the objective function and query it. We emphasize that this second file can run on **any other conda environment** (as long as you have `poli` installed, and the problem registered).

Let's make sure that the problem is registered. The list of registered problems is available on `poli.core.registry`'s function `get_problems() -> List[str]`:

```python
# querying_aloha.py
from poli.core.registry import get_problems

if __name__ == "__main__":
    print("our_aloha" in get_problems())

```

If you are running this script from an environment that has `poli`, and that has `aloha` as a registered problem, you will see:

```
True
```

Amazing. Let's remove this print. Now we can create an instance of the problem:

```python
# querying_aloha.py
import numpy as np

from poli import objective_factory

if __name__ == "__main__":
    # Creating an instance of the problem
    problem_info, f, x0, y0, run_info = objective_factory.create(
        name="our_aloha", caller_info=None, observer=None
    )
    print(x0, y0)

    # At this point, you can call f. This will create
    # a new isolated process, where the AlohaBlackBox
    # will run inside the conda environment poli_aloha.
    x1 = np.array(["F", "L", "E", "A", "S"]).reshape(1, -1)
    y1 = f(x1)
    print(x1, y1)

    f.terminate()
```

Running this script should give you

```
[['A' 'L' 'O' 'O' 'F']] [[3.]]
[['F' 'L' 'E' 'A' 'S']] [[1.]]
```

## Conclusion

In this tutorial you
1. Registered a black box objective function as a problem in `poli`, and
2. queried it somewhere else, without having to worry about the objective function's dependencies.

This is a trivial example, since the only dependency is numpy. In other examples you will see problems with more subtle dependencies (e.g. Java runtimes, torch, cheminformatics tools like `FoldX`, `RDKit`, or the therapeutics data commons...). [Take a look at all the available objective functions here](../objective_repository/all_objectives.md).

In the next chapters, we will define observers (i.e. a logging mechanism) and a simple "Problem Solver" (i.e. a black box optimization algorithm), we will wrap up by solving the `aloha` problem using the problem solver we define.
