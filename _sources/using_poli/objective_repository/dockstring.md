# dockstring

![Type of objective function: discrete inputs](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli dockstring](https://img.shields.io/badge/Environment-poli____dockstring-teal
)

## About

[dockstring](https://github.com/dockstring/dockstring) is an objective function for ligand design (i.e. for finding a small molecule that docks well against a certain protein) {cite:p}`GarciaOrtegon:dockstring:2022`. It uses OpenBabel and rdkit to prepare the ligand, and AutoDock Vina for docking.

Since the score given by Vina is supposed to be minimized, our implementation returns the negative.

## Prerequisites

None! The implementation of [dockstring](https://github.com/dockstring/dockstring) comes with batteries included. You don't even have to set up Autodock Vina. Unfortunately, it will only work on MacOS and Linux.

If you want to run the black box function directly, we would recommend installing (or having all the pre-requisites) of the `poli__dockstring` environment. See below.

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In the `poli__dockstring` environment

To run this black box function directly (which is useful for debugging, or when you are interested in setting breakpoints and inspecting the objects directly), we recommend you run it from inside the `poli__dockstring` environment, or make sure you satisfy all its requirements.

To create this environment, run

```bash
# From the root of the `poli` repository
conda env create --file src/poli/objective_repository/dockstring/environment.yml
```

Follow that with

```
conda activate poli__dockstring
```

Once you are in this environment (or in an environment that satisfies all its requirements), you can run the canonical example of risperidone and DRD3 docking:

```python
# from the poli__dockstring environment
import numpy as np

from poli.objective_repository import DockstringProblemFactory

if __name__ == "__main__":
    problem_factory = DockstringProblemFactory()

    f, x0, y0 = problem_factory.create(
        target_name="DRD2",
        string_representation="SMILES",  # Can be either SMILES or SELFIES
    )

    # The smiles for Risperidone
    risperidone_smiles = "CC1=C(C(=O)N2CCCCC2=N1)CCN3CCC(CC3)C4=NOC5=C4C=CC(=C5)F"

    x = np.array([list(risperidone_smiles)])
    
    # y is 11.9. Notice how this is -(what dockstring would give)
    y = f(x)
```

:::

:::{tab-item} In isolation

If you want `poli` to handle dependencies and environments under the hood, you can simply run

```python
import numpy as np

from poli import objective_factory

if __name__ == "__main__":
    problem_info, f, x0, y0, _ = objective_factory.create(
        name="dockstring",
        target_name="DRD2",
        string_representation="SMILES",
    )

    # The smiles for Risperidone
    risperidone_smiles = "CC1=C(C(=O)N2CCCCC2=N1)CCN3CCC(CC3)C4=NOC5=C4C=CC(=C5)F"

    x = np.array([list(risperidone_smiles)])
    
    # y is 11.9. Notice how this is -(what dockstring would give)
    y = f(x)

    f.terminate()
```

```{warning}
Registering the objective function in this way will create a `conda` environment called `poli__dockstring` with the relevant dependencies. You can find the exact environment description in the following file in the `poli` repository: `src/poli/objective_repository/dockstring/environment.yml`

```

:::

::::

