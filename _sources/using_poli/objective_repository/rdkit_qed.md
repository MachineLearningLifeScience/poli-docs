# Quantitative Estimate of Druglikeness (QED)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli chem](https://img.shields.io/badge/Environment-poli____chem-teal
)

## About

This objective function returns the Quantitative Estimate of Druglikeness (QED) using `RDKit`. You can specify whether you are measuring the QED of a SMILES string, or a SELFIES.

## Prerequisites

None. This black box should work out-of-the-box.

## How to run

You can either run this objective function in your current environment (assuming that you have the correct dependencies installed), or you can run it in an isolated environment.

::::{tab-set}

:::{tab-item} In current environment

You will have to install the following two dependencies:

```bash
pip install rdkit selfies
```

Then run

```python
import numpy as np
from poli import objective_factory

# How to create
f, x0, y0 = objective_factory.create(
    name="rdkit_qed",
    string_representation="SELFIES",  # Can be either SMILES or SELFIES
    force_register=True,
)

# Example input: a single carbon
x = np.array(["[C]"]).reshape(1, -1)

# Querying:
y = f(x)
print(y)  # Should be close to 0.35978494
```

:::

:::{tab-item} In isolation

If you want us to handle dependencies, run

```python
import numpy as np
from poli import objective_factory

# How to create
f, x0, y0 = objective_factory.create(
    name="rdkit_qed",
    alphabet=alphabet,
    string_representation="SELFIES",  # Can be either SMILES or SELFIES
    force_register=True,
)

# Example input: a single carbon
x = np.array(["[C]"]).reshape(1, -1)

# Querying:
y = f(x)
print(y)  # Should be close to 0.35978494
assert np.isclose(y, 0.35978494).all()

# Terminate the process.
f.terminate()
```

```{warning}
Registering the objective function in this way will create a `conda` environment called `poli__chem` with the relevant dependencies.
```

:::

::::
