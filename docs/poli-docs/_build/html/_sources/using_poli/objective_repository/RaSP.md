# Rapid Stability Predictions

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli rasp](https://img.shields.io/badge/Environment-poli____rasp-teal)

[*Rapid Stability Predictions* (RaSP)](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg) {cite:p}`Blaabjerg:RaSP:2023` predicts the stability of a protein using a supervised learning approach. Starting from features learned using self supervision {cite:p}`Boomsma:spherical_conv:2017`, RaSP learns to predict Rosetta scores using neural networks. The drawback being that only additive mutations could be computed simultaneously. We limit the edit distance to 1 (i.e. we only consider mutations that are one-away from the wildtype).

This objective function is quite similar to [`foldx_stability`](./foldx_stability.md), and can be considered a drop-in replacement for single mutations. Be aware that the scales are different. 

## Prerequisites

- A collection of `pdb` files you're interested in mutating.

However, your life would be easier if you run this black box objective function inside the `poli__rasp` environment. See below.

## How to run

Assuming you have [`3ned.pdb`](https://www.rcsb.org/structure/3ned) in the same directory as this script:

```python
from pathlib import Path
    from poli.objective_repository import RaspBlackBox, RaspProblemFactory

    wildtype_pdb_path = (
        Path(__file__).parent.parent / "static_files_for_tests" / "3ned.pdb"
    )

    # Creating the black box
    f = RaspBlackBox(wildtype_pdb_path=[wildtype_pdb_path])

    # Creating a problem
    problem = RaspProblemFactory().create(wildtype_pdb_path=[wildtype_pdb_path])
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

## Further reading

In the examples of `poli` you can find how to compute the saturation mutagenesis for a given protein at a given position.
