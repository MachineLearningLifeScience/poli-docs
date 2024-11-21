# DRD2 Docking (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli tdc](https://img.shields.io/badge/Environment-poli____tdc-teal
)

## About

This objective function computes the docking score of a small molecule (provided as a SMILES/SELFIES string) to the Dopamine Type 2 receptor. The underlying black box is actually using a trained random forest for classification {cite:p}`Olivecrona:DeNovoRL:2017`. We compute it using [the Therapeutics Data Common's oracle](https://tdcommons.ai/functions/oracles/#similaritydissimilarity) {cite:p}`Huang:TDC:2021`. This objective function is part of the Practical molecular Optimization benchmark {cite:p}`Gao:PMO:2022`.

## Prerequisites

None. This black box should run out-of-the-box.

## How to run

```python
import numpy as np
from poli.objective_repository import (
    DRD2ProblemFactory,
    DRD2BlackBox,
)

# Creating the black box
f = DRD2BlackBox(
    string_representation="SMILES" # SMILES by default, can be SELFIES
)

# Creating a problem
problem = DRD2ProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input: (taken from the TDC)
x = np.array(["CC(C)(C)[C@H]1CCc2c(sc(NC(=O)COc3ccc(Cl)cc3)c2C(N)=O)C1"])

# Querying:
y = f(x)
print(y)  # Should be close to [[0.001546]]
```

## How to cite

If you use this black box, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Olivecrona, Marcus, Thomas Blaschke, Ola Engkvist, and Hongming Chen. “Molecular De-Novo Design through Deep Reinforcement Learning.” Journal of Cheminformatics 9, no. 1 (September 4, 2017): 48. https://doi.org/10.1186/s13321-017-0235-x.

[2] Huang, Kexin, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf Roohani, Jure Leskovec, Connor W Coley, Cao Xiao, Jimeng Sun, and Marinka Zitnik. “Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development.” Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks, 2021.

[3] Gao, Wenhao, Tianfan Fu, Jimeng Sun, and Connor W. Coley.
    “Sample Efficiency Matters: A Benchmark for Practical Molecular Optimization,” 2022.
    https://openreview.net/forum?id=yCZRdI0Y7G.

[3] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{Olivecrona:DeNovoRL:2017,
  title={Molecular de-novo design through deep reinforcement learning},
  volume={9},
  ISSN={1758-2946},
  DOI={10.1186/s13321-017-0235-x},
  number={1},
  journal={Journal of Cheminformatics},
  author={Olivecrona, Marcus and Blaschke, Thomas and Engkvist, Ola and Chen, Hongming},
  year={2017},
  month=sep,
  pages={48},
  language={en}
}


@article{Huang:TDC:2021,
  title={Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development},
  author={Huang, Kexin and Fu, Tianfan and Gao, Wenhao and Zhao, Yue and Roohani, Yusuf and Leskovec, Jure and Coley,
          Connor W and Xiao, Cao and Sun, Jimeng and Zitnik, Marinka},
  journal={Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks},
  year={2021}
}


 @inproceedings{Gao:PMO:2022,
    title={Sample Efficiency Matters: A Benchmark for Practical Molecular Optimization},
    url={https://openreview.net/forum?id=yCZRdI0Y7G},
    author={Gao, Wenhao and Fu, Tianfan and Sun, Jimeng and Coley, Connor W.},
    year={2022},
    month=jun,
    language={en}
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
