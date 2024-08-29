# Rapid Stability Predictions

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli rasp](https://img.shields.io/badge/Environment-poli____rasp-teal)

[*Rapid Stability Predictions* (RaSP)](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg) {cite:p}`Blaabjerg:RaSP:2023` predicts the stability of a protein using a supervised learning approach. Starting from features learned using self supervision {cite:p}`Boomsma:spherical_conv:2017`, RaSP learns to predict Rosetta scores using neural networks. The drawback being that only additive mutations could be computed simultaneously. We limit the edit distance to 1 (i.e. we only consider mutations that are one-away from the wildtype).

This objective function is quite similar to [`foldx_stability`](./foldx_stability.md), and can be considered a drop-in replacement for single mutations. Be aware that the scales are different. 

Since our black boxes are meant to be maximized, we return **the negative** of what RaSP predicts.

## Prerequisites

- A collection of `pdb` files you're interested in mutating.

However, your life would be easier if you run this black box objective function inside the `poli__rasp` environment. [See here for an `environment.yml` file](https://github.com/MachineLearningLifeScience/poli/blob/71a307da47b1ebc64f00d1064bdea70e0fe8a57d/src/poli/objective_repository/rasp/environment.yml).

## How to run

Assuming you have [`3ned.pdb`](https://www.rcsb.org/structure/3ned) in the same directory as this script:

```python
from pathlib import Path
from poli.objective_repository import RaspBlackBox, RaspProblemFactory

wildtype_pdb_path = Path(__file__).parent  / "3ned.pdb"

# You can either
# (i) Create a black box
f = RaspBlackBox(
    wildtype_pdb_path=[wildtype_pdb_path],
    chains_to_keep=["A"],  #  <-- The chain in the pdb.
    additive=False,  #  <-- Whether to treat multiple mutations additively.
)

# or
# (ii) creating a problem
problem = RaspProblemFactory().create(
    wildtype_pdb_path=[wildtype_pdb_path]
    chains_to_keep=["A"],  #  <-- The chain in the pdb.
    additive=False,  #  <-- Whether to treat multiple mutations additively.
)
f, x0 = problem.black_box, problem.x0

# Querying:
print(f(x0))
```

## Warnings

:::{warning}

This objective function requires `clang` and `cmake`, which will be included in the `poli__rasp` conda environment. Make sure you are okay with this.

When the objective function is created, we will clone the [`reduce`](https://github.com/rlabduke/reduce) GitHub repository inside `~/.poli_objectives/rasp`, and we will compile it. We pin the version to the commit hash `bd23a0bf627ae9b08842102a5c2e9404b4a81924`.

This objective function also downloads several models (as `.pt` files) from [the RaSP repository](https://github.com/KULL-Centre/papers/tree/main/2022/ML-ddG-Blaabjerg-et-al/output).

Namely, we download `cavity_model_15.pt` and all `ds_models` and store them in `~/.poli_objectives/rasp`. These models are taken from the commit hash `3ccebe87e017b6bd737f88e1943557d128c85616`, and the files are checked against a pre-computed `md5` checksum.

:::


## How to cite

If you use this black box, we expect you to cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Blaabjerg, Lasse M, Maher M Kassem, Lydia L Good, Nicolas Jonsson, Matteo Cagiada, Kristoffer E Johansson, Wouter Boomsma, Amelie Stein, and Kresten Lindorff-Larsen. “Rapid Protein Stability Prediction Using Deep Learning Representations.” Edited by José D Faraldo-Gómez, Detlef Weigel, Nir Ben-Tal, and Julian Echave. eLife 12 (May 2023): e82593. https://doi.org/10.7554/eLife.82593.


[2] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```
@article{Blaabjerg:RaSP:2023,
  title        = {Rapid protein stability prediction using deep learning representations},
  volume       = {12},
  issn         = {2050-084X},
  doi          = {10.7554/eLife.82593},
  journal      = {eLife},
  publisher    = {eLife Sciences Publications, Ltd},
  author       = {Blaabjerg, Lasse M and Kassem, Maher M and Good, Lydia L and Jonsson, Nicolas and Cagiada, Matteo and Johansson, Kristoffer E and Boomsma, Wouter and Stein, Amelie and Lindorff-Larsen, Kresten},
  editor       = {Faraldo-Gómez, José D and Weigel, Detlef and Ben-Tal, Nir and Echave, Julian},
  year         = {2023},
  month        = may,
  pages        = {e82593}
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

In the examples of `poli` you can find how to compute the saturation mutagenesis for a given protein at a given position.
