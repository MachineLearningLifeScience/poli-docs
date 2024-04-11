# Albuterol Similarity (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli tdc](https://img.shields.io/badge/Environment-poli____tdc-teal
)

## About

This objective function computes the similarity of a given SMILES/SELFIES to [Albuterol](https://pubchem.ncbi.nlm.nih.gov/compound/2083), and is part of the **similarity** family of GuacaMol {cite:p}`Brown:guacamol:2019` benchmark. We compute it using [the Therapeutics Data Common's oracle](https://tdcommons.ai/functions/oracles/#similaritydissimilarity) {cite:p}`Huang:TDC:2021`.

## Prerequisites

None. This black box should run out-of-the-box.

## How to run

```python
import numpy as np
from poli.objective_repository import (
    AlbuterolSimilarityProblemFactory,
    AlbuterolSimilarityBlackBox,
)

# Creating the black box
f = AlbuterolSimilarityBlackBox(
    string_representation="SMILES" # SMILES by default, can be SELFIES
)

# Creating a problem
problem = AlbuterolSimilarityProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input: (taken from the TDC)
x = np.array(["CC(C)(C)[C@H]1CCc2c(sc(NC(=O)COc3ccc(Cl)cc3)c2C(N)=O)C1"])

# Querying:
y = f(x)
print(y)  # Should be close to [[0.2772277]]
```

## How to cite

If you use this black box, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Brown, Nathan, Marco Fiscato, Marwin H.S. Segler, and Alain C. Vaucher. “GuacaMol: Benchmarking Models for de Novo Molecular Design.” Journal of Chemical Information and Modeling 59, no. 3 (March 25, 2019): 1096–1108. https://doi.org/10.1021/acs.jcim.8b00839.

[2] Huang, Kexin, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf Roohani, Jure Leskovec, Connor W Coley, Cao Xiao, Jimeng Sun, and Marinka Zitnik. “Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development.” Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks, 2021.

[3] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{Brown:guacamol:2019,
title={GuacaMol: Benchmarking Models for de Novo Molecular Design},
    volume={59},
    ISSN={1549-9596,
    1549-960X},
    DOI={10.1021/acs.jcim.8b00839},
    number={3},
    journal={Journal of Chemical Information and Modeling},
    author={Brown, Nathan and Fiscato, Marco and Segler, Marwin H.S. and Vaucher, Alain C.},
    year={2019},
    month=mar,
    pages={1096–1108},
    language={en} }


@article{Huang:TDC:2021,
  title={Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development},
  author={Huang, Kexin and Fu, Tianfan and Gao, Wenhao and Zhao, Yue and Roohani, Yusuf and Leskovec, Jure and Coley,
          Connor W and Xiao, Cao and Sun, Jimeng and Zitnik, Marinka},
  journal={Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks},
  year={2021}
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
