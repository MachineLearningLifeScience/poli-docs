# Synthetic Accessibility (using TDC)

![Type of objective function: discrete](https://img.shields.io/badge/Type-discrete_inputs-blue)
![Environment to run this objective function: poli tdc](https://img.shields.io/badge/Environment-poli____tdc-teal
)

## About

This objective function computes the synthetic accesibility of a small molecule {cite:p}`Ertl:SA:2009,Polykovskiy:MOSES:2020` using [the Therapeutics Data Common's oracle](https://tdcommons.ai/functions/oracles/#synthetic-accessibility-sa) {cite:p}`Huang:TDC:2021` (which uses RDKit internally).

## Prerequisites

None. This black box should run out-of-the-box.

## How to run

```python
import numpy as np
from poli.objective_repository import SAProblemFactory, SABlackBox

# Creating the black box
f = SABlackBox()

# Creating a problem
problem = SAProblemFactory().create()
f, x0 = problem.black_box, problem.x0

# Example input: (taken from the TDC)
x = np.array(["CCNC(=O)c1ccc(NC(=O)N2CC[C@H](C)[C@H](O)C2)c(C)c1"])

# Querying:
y = f(x)
print(y)  # Should be close to 2.85483733
```

## How to cite

If you use this black box, we expect that you cite the following resources:

::::{tab-set}

:::{tab-item} References as text

[1] Ertl, Peter, and Ansgar Schuffenhauer. “Estimation of Synthetic Accessibility Score of Drug-like Molecules Based on Molecular Complexity and Fragment Contributions.” Journal of Cheminformatics 1, no. 1 (June 10, 2009): 8. https://doi.org/10.1186/1758-2946-1-8.


[2] Polykovskiy, Daniil, Alexander Zhebrak, Benjamin Sanchez-Lengeling, Sergey Golovanov, Oktai Tatanov, Stanislav Belyaev, Rauf Kurbanov, et al. “Molecular Sets (MOSES): A Benchmarking Platform for Molecular Generation Models.” Frontiers in Pharmacology 11 (2020). https://www.frontiersin.org/articles/10.3389/fphar.2020.565644.


[3] Huang, Kexin, Tianfan Fu, Wenhao Gao, Yue Zhao, Yusuf Roohani, Jure Leskovec, Connor W Coley, Cao Xiao, Jimeng Sun, and Marinka Zitnik. “Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development.” Proceedings of Neural Information Processing Systems, NeurIPS Datasets and Benchmarks, 2021.

[4] González-Duque, M., Bartels, S., & Michael, R. (2024). poli: a libary of discrete sequence objectives [Computer software]. https://github.com/MachineLearningLifeScience/poli


:::

:::{tab-item} References as `BibTeX`

```

@article{Ertl:SA:2009,
    title={Estimation of synthetic accessibility score of drug-like molecules based on molecular complexity and fragment contributions},
    volume={1},
    ISSN={1758-2946},
    DOI={10.1186/1758-2946-1-8},
    number={1},
    journal={Journal of Cheminformatics},
    author={Ertl, Peter and Schuffenhauer, Ansgar},
    year={2009},
    month=jun,
    pages={8},
    language={en}
}

@article{Polykovskiy:MOSES:2020,
    title={Molecular Sets (MOSES): A Benchmarking Platform for Molecular Generation Models},
    volume={11},
    ISSN={1663-9812},
    url={https://www.frontiersin.org/articles/10.3389/fphar.2020.565644},
    author={Polykovskiy, Daniil and Zhebrak, Alexander and Sanchez-Lengeling, Benjamin and Golovanov, Sergey and Tatanov, Oktai and Belyaev, Stanislav and Kurbanov, Rauf and Artamonov, Aleksey and Aladinskiy, Vladimir and Veselov, Mark and Kadurin, Artur and Johansson, Simon and Chen, Hongming and Nikolenko, Sergey and Aspuru-Guzik, Alán and Zhavoronkov, Alex},
    year={2020}
}

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

