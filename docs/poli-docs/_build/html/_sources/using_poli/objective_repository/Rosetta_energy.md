# Rosetta Energy Stability Predictions

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli rosetta_energy](https://img.shields.io/badge/Environment-poli____rosetta_energy-teal)

[*Rosetta Energy*](https://www.pyrosetta.orgg) {cite:p}`Chaudhury:PyRosetta:2010` (following among others {cite:p}`Leaverfay:Rosetta3:2011`, {cite:p}`Simons:CaspIII:1999` with a more comprehensive list [here](https://docs.rosettacommons.org/docs/latest/getting_started/Rosetta-canon)) predicts the stability of a protein from a change in Gibbs free energy ($\Delta\Delta$G) from a change in protein residue(s) via a scoring function.
This is initially Rosetta specific energy units (REUs), which are scaled and a difference to the reference (ie. wild-type) is taken.
An initial structure is required in the form of a *PDB* file.
We do not limit the edit distance and free form optimization can be conducted.

This objective function is comparable in use to [`foldx_stability`](./foldx_stability.md).

## Prerequisites

- A PyRosetta4 license,
- A `pdb` file you're interested in mutating.

We recommend to run this black box objective function inside the `poli__rosetta_energy` environment. [See here for an `environment.yml` file](https://github.com/MachineLearningLifeScience/poli/blob/dev/src/poli/objective_repository/rosetta_energy/environment.yml).

## How to run

Assuming you have [`3ned.pdb`](https://www.rcsb.org/structure/3ned) in the same directory as this script:

```python
from pathlib import Path
from poli.objective_repository import RosettaEnergyBlackBox, RosettaEnergyProblemFactory

wildtype_pdb_path = Path(__file__).parent  / "3ned.pdb"

# Minimal viable instantiation
f = RosettaEnergyBlackBox(
    wildtype_pdb_path=wildtype_pdb_path,
)

# Advanced instantiation
# (i) Create a black box
f = RosettaEnergyBlackBox(
    wildtype_pdb_path=wildtype_pdb_path,
    score_function="default",  #  <-- The scoring function to use (default is ref2015_cart).
    unit="DDG",   #  <-- output unit (REU, DREU, DDG).
    clean=True,   #  <-- clean PDB file.
    relax=True,   #  <-- use relax function of the protocol.
    pack=True,    #  <-- use pack function of the protocol.
)

# or
# (ii) creating a problem
problem = RosettaEnergyProblemFactory().create(
    wildtype_pdb_path=[wildtype_pdb_path]
    chains_to_keep=["A"],  #  <-- The chain in the pdb.
    additive=False,  #  <-- Whether to treat multiple mutations additively.
)
f, x0 = problem.black_box, problem.x0

# Querying:
print(f(x0))
```

### Additional Information
#### Output units
Available are: `REU` , `DREU`, `DDG` .


Standard Rosetta software would provide energy units: **REU**s as output.
If you take the difference to the wild-type (/reference) sequence you obtain a $\Delta$**REU** output.

If you apply a scaling factor you obtain **DDG** values.
We follow the (at the time of writing) current default of $2.9$, as described in {cite:p}`Park:Scale:2016`.

You can modify the factor via the `conversion_factor` flag.

#### Scoring functions

Available choices: `ref2015`, `ref2015_cart` (default), `centroid`, `fa` (PyRosetta spec), `franklin2019` (WIP).


These scoring functions are subject to change in the future, especially what the recommended default is. 
Why and how these functions have been deemed valid and set as defaults we defer to the [RosettaCommons](https://docs.rosettacommons.org/docs/latest/rosetta_basics/scoring/score-types) and related publications (see link).


Generally, if a `_cart` suffix is present, a *cartesian* protocol is invoked.


The current defaults are published in {cite:p}`Park:Scale:2016` and {cite:p}`Alford:ref2015:2017`.


## Warnings

:::{warning}

This objective function requires a valid license (for example free for academic use) which will inquired on first use.


The moment you modify: `conversion_factor`, `score_function`, `cycle`, `pack` on instantiation of the black-box we trust you know what you're doing.

:::


## How to cite

If you use this black box, we expect you to cite at least the following resources - see below.
We further recommend to cite the scoring functions used.

::::{tab-set}

:::{tab-item} References as text

[1] Chaudhury, Sidhartha, Sergey Lyskov, and Jeffrey J. Gray. "PyRosetta: a script-based interface for implementing molecular modeling algorithms using Rosetta." Bioinformatics 26 (March 2010): 689-691. https://doi.org/10.1093/bioinformatics/btq007

[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```
@article{Chaudhury:PyRosetta:2010,
  title={PyRosetta: a script-based interface for implementing molecular modeling algorithms using Rosetta},
  author={Chaudhury, Sidhartha and Lyskov, Sergey and Gray, Jeffrey J},
  journal={Bioinformatics},
  volume={26},
  number={5},
  pages={689--691},
  year={2010},
  publisher={Oxford University Press}
}

@incollection{Leaverfay:Rosetta3:2011,
title = {Chapter nineteen - Rosetta3: An Object-Oriented Software Suite for the Simulation and Design of Macromolecules},
editor = {Michael L. Johnson and Ludwig Brand},
series = {Methods in Enzymology},
publisher = {Academic Press},
volume = {487},
pages = {545-574},
year = {2011},
booktitle = {Computer Methods, Part C},
issn = {0076-6879},
doi = {https://doi.org/10.1016/B978-0-12-381270-4.00019-6},
url = {https://www.sciencedirect.com/science/article/pii/B9780123812704000196},
author = {Andrew Leaver-Fay and Michael Tyka and Steven M. Lewis and Oliver F. Lange and James Thompson and Ron Jacak and Kristian W. Kaufman and P. Douglas Renfrew and Colin A. Smith and Will Sheffler and Ian W. Davis and Seth Cooper and Adrien Treuille and Daniel J. Mandell and Florian Richter and Yih-En Andrew Ban and Sarel J. Fleishman and Jacob E. Corn and David E. Kim and Sergey Lyskov and Monica Berrondo and Stuart Mentzer and Zoran Popović and James J. Havranek and John Karanicolas and Rhiju Das and Jens Meiler and Tanja Kortemme and Jeffrey J. Gray and Brian Kuhlman and David Baker and Philip Bradley},
}

@article{Simons:CaspIII:1999,
  title={Ab initio protein structure prediction of CASP III targets using ROSETTA},
  author={Simons, Kim T and Bonneau, Rich and Ruczinski, Ingo and Baker, David},
  journal={Proteins: Structure, Function, and Bioinformatics},
  volume={37},
  number={S3},
  pages={171--176},
  year={1999},
  publisher={Wiley Online Library}
}

@article{Park:Scale:2016,
  title={Simultaneous optimization of biomolecular energy functions on features from small molecules and macromolecules},
  author={Park, Hahnbeom and Bradley, Philip and Greisen Jr, Per and Liu, Yuan and Mulligan, Vikram Khipple and Kim, David E and Baker, David and DiMaio, Frank},
  journal={Journal of chemical theory and computation},
  volume={12},
  number={12},
  pages={6201--6212},
  year={2016},
  publisher={ACS Publications}
}

@article{Alford:ref2015:2017,
  title={The Rosetta all-atom energy function for macromolecular modeling and design},
  author={Alford, Rebecca F and Leaver-Fay, Andrew and Jeliazkov, Jeliazko R and O’Meara, Matthew J and DiMaio, Frank P and Park, Hahnbeom and Shapovalov, Maxim V and Renfrew, P Douglas and Mulligan, Vikram K and Kappel, Kalli and others},
  journal={Journal of chemical theory and computation},
  volume={13},
  number={6},
  pages={3031--3048},
  year={2017},
  publisher={ACS Publications}
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


## Further reading

1. [The Manual](https://graylab.jhu.edu/pyrosetta/downloads/documentation/PyRosetta_Manual.pdf).
2. [Official PyRosetta Docs](https://graylab.jhu.edu/PyRosetta.documentation/pyrosetta.html).
