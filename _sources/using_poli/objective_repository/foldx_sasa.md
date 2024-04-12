# Protein solvent accessibility (using `foldx`)
![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli protein](https://img.shields.io/badge/Environment-poli____protein-teal
)

## About

This objective function returns the solvent accesible surface area (SASA) of a wildtype and its mutations using `foldx` and `biopython`.

:::{note}

If you are interested in computing **both** a protein's stability and it's SASA score, try `foldx_stability_and_sasa` instead! Just change the `name` in the `create` method below.

:::

## Prerequisites

- [Have `foldx` installed](../../understanding_foldx/00-installing-foldx.md), and available in your home directory. We expect the following files to be there:
  - `~/foldx/foldx`: the binary. You might need to rename it.
  - `~/foldx/rotabase.txt`: a text file necessary for `foldx` to run (only if you are using v4 of `foldx`).
- A (list of) `wildtype_pdb_file`: a (repaired) pdb file of the wildtype.

:::{admonition} We can repair the file for you
:class: dropdown

By default, we will assume you are passing a repaired `pdb` file to us (indeed, we check if the filename contains `_Repair`). If you want us to repair the file for you and keep it in a cache, you can add the `eager_repair=True` keyword argument to the `create` method.

Otherwise, pre-repair your files using e.g.

```bash
~/foldx/foldx --command=RepairPDB --pdb your_file.pdb --water -CRYSTAL --pH 7.0
```

In our repairing process, we also remove heteroatoms using [`pdbtools`](https://www.bonvinlab.org/pdb-tools/).

:::

## How to run

```python
from pathlib import Path
    
from poli.objective_repository import FoldXSASAProblemFactory, FoldXSASABlackBox

wildtype_pdb_path = Path("path/to/your/wildtype_Repair.pdb")

# Creating the black box
f = FoldXSASABlackBox(wildtype_pdb_path=[wildtype_pdb_path])

# Creating a problem
problem = FoldXSASAProblemFactory().create(wildtype_pdb_path=[wildtype_pdb_path])
f, x0 = problem.black_box, problem.x0

# Example evaluation: SASA of your wildtype
print(f(x0))
```

## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Schymkowitz, Joost, Jesper Borg, Francois Stricher, Robby Nys, Frederic Rousseau, and Luis Serrano. “The FoldX Web Server: An Online Force Field.” Nucleic Acids Research 33, no. Web Server issue (July 1, 2005): W382–88. https://doi.org/10.1093/nar/gki387.

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

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

