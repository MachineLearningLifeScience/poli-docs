# GSK3β (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli tdc](https://img.shields.io/badge/Environment-poli____tdc-teal
)

## About

An interface to [the Therapeutics Data Common's oracle GSK3β](https://tdcommons.ai/functions/oracles/#glycogen-synthase-kinase-3-beta-gsk3β) {cite:p}`Huang:TDC:2021`. The underlying black box is actually using a trained random forest for classification {cite:p}`Jin:MOInterpretable:2020,Li:MOConditional:2018`. This objective function is part of the Practical molecular Optimization benchmark {cite:p}`Gao:PMO:2022`.

## Prerequisites

None. This black box should run out-of-the-box.

## How to run

```python
import numpy as np
from poli.objective_repository import (
    GSK3BetaProblemFactory,
    GSK3BetaBlackBox,
)

# Creating the black box
f = GSK3BetaBlackBox(
    string_representation="SMILES" # SMILES by default, can be SELFIES
)

# Creating a problem
problem = GSK3BetaProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input: (taken from the TDC)
x = np.array(["CC(C)(C)[C@H]1CCc2c(sc(NC(=O)COc3ccc(Cl)cc3)c2C(N)=O)C1"])

# Querying:
y = f(x)
print(y)  # Should be close to [[0.03]]
```

## How to cite

If you use this black box, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Li, Yibo, Liangren Zhang, and Zhenming Liu. “Multi-Objective de Novo Drug Design with Conditional Graph Generative Model.” Journal of Cheminformatics 10, no. 1 (July 24, 2018): 33. https://doi.org/10.1186/s13321-018-0287-6.

[2] Jin, Wengong, Regina Barzilay, and Tommi Jaakkola. “Multi-Objective Molecule Generation Using Interpretable Substructures.” Proceedings of the 37 Th International Conference on Machine Learning PMLR 119 (2020).

[3] Huang, Kexin, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf Roohani, Jure Leskovec, Connor W Coley, Cao Xiao, Jimeng Sun, and Marinka Zitnik. “Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development.” Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks, 2021.

[4] Gao, Wenhao, Tianfan Fu, Jimeng Sun, and Connor W. Coley.
    “Sample Efficiency Matters: A Benchmark for Practical Molecular Optimization,” 2022.
    https://openreview.net/forum?id=yCZRdI0Y7G.

[5] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{Li:MOConditional:2018,
  title={Multi-objective de novo drug design with conditional graph generative model},
  volume={10},
  ISSN={1758-2946},
  DOI={10.1186/s13321-018-0287-6},
  number={1},
  journal={Journal of Cheminformatics},
  author={Li, Yibo and Zhang, Liangren and Liu, Zhenming},
  year={2018},
  month=jul,
  pages={33},
  language={en}
}


@article{Jin:MOInterpretable:2020,
     title={Multi-Objective Molecule Generation using Interpretable Substructures},
     volume={119},
     journal={Proceedings of the 37 th International Conference on Machine Learning PMLR},
     author={Jin, Wengong and Barzilay, Regina and Jaakkola, Tommi},
     year={2020},
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
