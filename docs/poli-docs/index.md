# poli 🧪: a library of discrete objective functions

[![Testing (conda, python 3.9)](https://github.com/MachineLearningLifeScience/poli/actions/workflows/python-tox-testing-including-conda.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli/actions/workflows/python-tox-testing-including-conda.yml) [![Test (conda, python 3.9)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing.yml/badge.svg)](https://github.com/MachineLearningLifeScience/poli-baselines/actions/workflows/python-tox-testing.yml)

[poli](https://github.com/MachineLearningLifeScience/poli) is a library of discrete objective functions for benchmarking optimization algorithms. Examples include:
- 🔬 **stability** of mutations from a wildtype protein (using [foldx](https://foldxsuite.crg.eu/) or [rasp](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg)).
- 🧪 **docking scores** of ligands to proteins (using [dockstring](https://github.com/dockstring/dockstring), [pyscreener](https://github.com/coleygroup/pyscreener) and [pytdc](https://tdcommons.ai/functions/oracles/)).
- 💊 **druglikeness** or **synthetic acccesibility** of small molecules (using [rdkit](https://github.com/rdkit/rdkit) and [pytdc](https://tdcommons.ai/functions/oracles/)).

Some of `poli`'s features:
- 🔲 **isolation** of black box function calls inside conda environments. Don't worry about clashes w. black box requirements, poli will create the relevant conda environments for you.
- 🗒️ **logging** logic at the black box `__call__` level using observers.
-  A numpy interface. Inputs are `np.array`s of strings, outputs are `np.array`s of floats.
- `SMILES` and `SELFIES` support for small molecule manipulation.

This documentation also discusses [`poli-baselines`](https://github.com/MachineLearningLifeScience/poli-baselines), a collection of optimizers of these discrete black box functions which is currently in alpha stage.

## Getting started

A good place to start is the next chapter! [Go to Getting Started](./getting_started/getting_started.md).

To install `poli` and `poli-baselines`, we recommend creating a fresh conda environment

```bash
conda create -n poli-base python=3.9
conda activate poli-base
pip install git+https://github.com/MachineLearningLifeScience/poli.git@dev
pip install git+https://github.com/MachineLearningLifeScience/poli-baselines.git@main
```

`poli` also runs on Google Colab. [Here is a small example of how to run one of the objective functions.](https://colab.research.google.com/drive/1-IISCebWYfu0QhuCJ11wOag8aKOiPtls?usp=sharing).

## Black-box objective functions

[For a full list, click here](./using_poli/objective_repository/all_objectives.md).

### Toy problems

::::{grid}
:gutter: 3

:::{grid-item-card} White noise
:link: ./using_poli/objective_repository/white_noise.html
:columns: 6
White noise drawn from a unit Gaussian
:::

:::{grid-item-card} Aloha
:link: ./using_poli/objective_repository/aloha.html
:columns: 6
A toy example about optimizing 5-letter words to spell "ALOHA"
:::

:::{grid-item-card} Toy continuous problems
:link: ./using_poli/objective_repository/toy_continuous_problems.html
:columns: 6
The usual benchmark functions for continuous optimization (e.g. `easom`, or `ackley_function_01`)
:::

::::

### Small molecules

::::{grid}
:gutter: 3

:::{grid-item-card} Quantitative Estimate of Druglikeness (QED)
:link: ./using_poli/objective_repository/rdkit_qed.html
:columns: 6
Computing the QED using `RDKit`.
:::

:::{grid-item-card} Log-solubility (LogP)
:link: ./using_poli/objective_repository/rdkit_logp.html
:columns: 6
Computing the log-quotient of solubilities using `RDKit`.
:::

:::{grid-item-card} Penalized Log-solubility (LogP, using `lambo`)
:link: ./using_poli/objective_repository/penalized_logp_lambo.html
:columns: 6
Computing the penalized log-quotient of solubilities using `lambo`'s implementation.
:::

:::{grid-item-card} DRD3 (or 3pbl) docking (using `tdc`)
:link: ./using_poli/objective_repository/drd3_docking.html
:columns: 6
A wrapper around the Therapeutics Data Commons implmenetation of `3pbl` docking.
:::

:::{grid-item-card} Synthetic Accessibility (SA, using `tdc`)
:link: ./using_poli/objective_repository/sa_tdc.html
:columns: 6
A wrapper around the Therapeutics Data Commons implmenetation of the synthetic accessibility oracle.
:::

::::

### Proteins

::::{grid}
:gutter: 3

:::{grid-item-card} Protein Stability (using `foldx`)
:link: ./using_poli/objective_repository/foldx_stability.html
:columns: 6
Stability of mutations of a wildtype using `foldx`
:::

:::{grid-item-card} Protein SASA score (using `foldx`)
:link: ./using_poli/objective_repository/foldx_sasa.html
:columns: 6
Solvent accessibility of mutations of a wildtype using `foldx`
:::

:::{grid-item-card} Protein Stability (using `RaSP`)
:link: ./using_poli/objective_repository/RaSP.html
:columns: 6
Rapid Stability Predictions of single mutations from a wildtype.
:::

:::{grid-item-card} RFP Fluorescence Protein Stability (using `lambo`)
:link: ./using_poli/objective_repository/foldx_rfp_lambo.html
:columns: 6
LaMBO Fluorescence (RFP) by stability and solvent-accessible surface area.
:::

::::


## Black-box optimization algorithms

On top of `poli`, we provide `poli-baselines`, a collection of **black-box optimization algorithms** (focusing especially on *discrete* sequences). Examples include

::::{grid}
:gutter: 3

:::{grid-item-card} Random Mutations
:link: ./using_poli_baselines/random_mutations.html
:columns: 6
Optimizing a discrete sequence by performing random mutations
:::

:::{grid-item-card} CMA-ES
:link: ./using_poli_baselines/cma_es.html
:columns: 6
An evolutionary strategy for continuous problems
:::

:::{grid-item-card} Bayesian Optimization
:link: ./using_poli_baselines/latent_space_bo.html
:columns: 6
A vanilla implementation of Bayesian Optimization using `botorch`.
:::

:::{grid-item-card} Line Bayesian Optimization
:link: ./using_poli_baselines/latent_space_bo.html
:columns: 6
A version of Bayesian Optimization where the acquisition is optimized over a line.
:::

::::

## Cite us and other relevant work

If you use `poli`, we encourage you to cite us

```
@software{GonzalezDuqueBartelsMichael:poli:2024,
author = {González-Duque, Miguel and Bartels, Simon and Michael, Richard},
month = jan,
title = {{poli: a libary of discrete sequence objectives}},
url = {https://github.com/MachineLearningLifeScience/poli},
version = {0.0.1},
year = {2024}
}
```

If you use certain black boxes, we also recommend citing the original work:

|Black box|Reference(s)|
|---------|---------|
|`dockstring`|[(García-Ortegón et al. 2022)](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01334)|
|`drd3_docking`|[(Graff, Shakhnovich and Coley 2020)](https://pubs.acs.org/doi/10.1021/acs.jcim.1c01334), [(Graff and Coley 2022)](https://joss.theoj.org/papers/10.21105/joss.03950), [(Huang et al. 2022)](https://www.nature.com/articles/s41589-022-01131-2)|
|`foldx_*`|[(Schymkowitz et al. 2005)](https://academic.oup.com/nar/article/33/suppl_2/W382/2505499)|
|`gfp_cbas`|[(Brookes, Park and Listgarten 2019)](https://proceedings.mlr.press/v97/brookes19a.html)|
|`gfp_select`|[(Brookes, Park and Listgarten 2019)](https://proceedings.mlr.press/v97/brookes19a.html)|
|`penalized_logp_lambo`|[(Stanton et al. 2022)](https://github.com/samuelstanton/lambo)|
|`rasp`|[(Blaabjerg et al. 2022)](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg)|
|`rdkit_*`|[(rdkit)](https://github.com/rdkit/rdkit)|
|`rfp_foldx_*`|[(Schymkowitz et al. 2005)](https://academic.oup.com/nar/article/33/suppl_2/W382/2505499), [(Stanton et al. 2022)](https://github.com/samuelstanton/lambo)|
|`sa_tdc`|[(Huang et al. 2022)](https://www.nature.com/articles/s41589-022-01131-2), [(rdkit)](https://github.com/rdkit/rdkit), [(Ertl and Schuffenhauer 2009)](https://link.springer.com/article/10.1186/1758-2946-1-8)|
|`super_mario_bros`|[(Volz et al. 2018)](https://github.com/CIGbalance/DagstuhlGAN), [(González-Duque 2023)](https://github.com/miguelgondu/minimal_VAE_on_Mario) |
|`toy_continuous_problem`|[(Al-Roomi 2015)](https://www.al-roomi.org/benchmarks/unconstrained), [(Surjanovic and Bingham 2013)](https://www.sfu.ca/~ssurjano/optimization.html) |


## Contribute problems or solvers

These are a couple of guides about how to contribute a new problem factory (i.e. black-box objective function), or a new optimization algorithm.

::::{grid}
:gutter: 3

:::{grid-item-card} Contribute a new problem
:link: ./contributing/a_new_problem.html
:columns: 6
A guide to contributing a new problem to the repository.
:::

:::{grid-item-card} Contribute a new solver
:link: ./contributing/a_new_solver.html
:columns: 6
How to contribute a new black-box optimization algorithm.
:::


::::

