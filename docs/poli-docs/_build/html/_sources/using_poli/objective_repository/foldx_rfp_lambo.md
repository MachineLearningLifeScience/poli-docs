# Protein (RFP) stability and SASA (using `foldx`,`lambo`)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli protein](https://img.shields.io/badge/Environment-poli____lambo-teal)

## About

This objective function returns stability using `foldx` and SASA, _exactly_ as done in the `lambo` implementation.

## Prerequisites

### `foldx`

We need you to have `foldx` installed, and available in your home directory. We expect the following files to be there:
  - `~/foldx/foldx`: the binary. You might need to rename it.
  - `~/foldx/rotabase.txt`: a text file necessary for `foldx` to run.

### Python environment

We recommend that you have [cloned and installed the `lambo` repository](https://github.com/samuelstanton/lambo). Since there are some files we can't install automatically using `pip install git+...`, we recommend that you create a `conda` environment for the lambo tasks:

```
# From the root of the poli repository
conda env create --file src/poli/objective_repository/foldx_rfp_lambo/environment.yml
```

Activate the environment you just created using
```
conda activate poli__lambo
```
### `lambo`

We also need `lambo`'s tasks to be available in Python's path for `poli__lambo`:

```bash
# In the poli__lambo environment
git clone https://github.com/samuelstanton/lambo    # For reference, we use 431b052
cd lambo
pip install -e .  
```

In particular, we need
- `lambo.tasks.proxy_rfp.proxy_rfp.ProxyRFPTask`
- the rfp data: see `~/lambo/assets/fpbase`

Make sure the data is avaliable.

:::{admonition} We can install `lambo` automatically
:class: dropdown

These steps can be skipped. If so, we will install LaMBO automatically and download the relevant files using `PyGithub`. That being said, the API of GitHub limits queries if you are doing anonymous queries. If you decide to skip installing lambo, we recommend that you add an environment variable called `GITHUB_TOKEN_FOR_POLI` whose value is a personal token. [See how to create one here.](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token)

:::

## How to run

You can only run this objective function either in the `poli__lambo` environment, or as an isolated process (which runs this environment underneath).

::::{tab-set}

:::{tab-item} (Isolated) in the `poli__lambo` environment

After the setup described above, you can simply run the following code from 

```python
from pathlib import Path

import numpy as np

from poli import objective_factory

# How to create
f, x0, y0 = objective_factory.create(
    name="foldx_rfp_lambo",
)

# Example input:
print(x0)

# Querying:
print(y0)  # [[-11189.00587946    -39.8155    ], ...]
```

You could also pass an `problem: ProblemSetupInformation` to the create method. For the alphabet reference by default, [we use this encoding](https://github.com/MachineLearningLifeScience/poli/blob/44cad2a5c95f209aeb24d4893d162b3359ca91a3/src/poli/core/util/proteins/defaults.py#L1).

:::

::::

## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Stanton, Samuel, Wesley Maddox, Nate Gruver, Phillip Maffettone, Emily Delaney, Peyton Greenside, and Andrew Gordon Wilson. “Accelerating Bayesian Optimization for Biological Sequence Design with Denoising Autoencoders.” arXiv, July 12, 2022. http://arxiv.org/abs/2203.12742.

[2] Schymkowitz, Joost, Jesper Borg, Francois Stricher, Robby Nys, Frederic Rousseau, and Luis Serrano. “The FoldX Web Server: An Online Force Field.” Nucleic Acids Research 33, no. Web Server issue (July 1, 2005): W382–88. https://doi.org/10.1093/nar/gki387.

[3] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{stanton:LaMBO:2022,
  title   = {Accelerating Bayesian Optimization for Biological Sequence Design with Denoising Autoencoders},
  author  = {Stanton, Samuel and Maddox, Wesley and Gruver, Nate and Maffettone, Phillip and Delaney, Emily and Greenside, Peyton and Wilson, Andrew Gordon},
  journal = {arXiv preprint arXiv:2203.12742},
  year    = {2022}
}

@article{Schymkowitz:foldx:2005, title={The FoldX web server: an online force field},
  volume={33},
  ISSN={0305-1048},
  DOI={10.1093/nar/gki387},
  journal={Nucleic Acids Research},
    author={Schymkowitz, Joost and Borg, Jesper and Stricher, Francois and Nys, Robby and Rousseau, Frederic and Serrano, Luis},
    year={2005},
    month=jul,
    pages={W382–W388}
}

@software{Gonzalez-Duque:poli:2024,
author = {González-Duque, Miguel and Bartels, Simon and Michael, Richard},
month = jan,
title = {{poli: a libary of discrete sequence objectives}},
url = {https://github.com/MachineLearningLifeScience/poli},
version = {0.0.1},
year = {2024}
}

```

:::

::::
