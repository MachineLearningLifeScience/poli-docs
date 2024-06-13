# poli 🧪: a library of discrete objective functions

[poli](https://github.com/MachineLearningLifeScience/poli) is a library of discrete objective functions for benchmarking optimization algorithms. Examples include:
- 🔬 **stability** of mutations from a wildtype protein (using [foldx](https://foldxsuite.crg.eu/) or [rasp](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg)).
- 🧪 **docking scores** of ligands to proteins (using [dockstring](https://github.com/dockstring/dockstring), [pyscreener](https://github.com/coleygroup/pyscreener) and [pytdc](https://tdcommons.ai/functions/oracles/)).
- 💊 **druglikeness** or **synthetic acccesibility** of small molecules (using [rdkit](https://github.com/rdkit/rdkit) and [pytdc](https://tdcommons.ai/functions/oracles/)).

Some of `poli`'s features:
- 🔲 **isolation** of black box function calls inside conda environments. Don't worry about clashes w. black box requirements, poli will create the relevant conda environments for you.
- 🗒️ **logging** each black box call using observers.
-  A numpy interface. Inputs are `np.array`s of strings, outputs are `np.array`s of floats.
- `SMILES` and `SELFIES` support for small molecule manipulation.

This documentation also discusses [`poli-baselines`](https://github.com/MachineLearningLifeScience/poli-baselines), a collection of optimizers of these discrete black box functions.

:::{admonition} We are running a benchmark!

Using `poli` and `poli-baselines`, [we are running a benchmark comparing high-dimensional Bayesian optimization algorithms for discrete sequence](https://machinelearninglifescience.github.io/hdbo_benchmark/).

:::

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

:::{grid-item-card} Albuterol Similarity (using `tdc`)
:link: ./using_poli/objective_repository/albuterol_similarity.html
:columns: 6
The Therapeutics Data Commons' implementation of the Albuterol similarity oracle of GuacaMol.
:::

:::{grid-item-card} Amlodipine MPO (using `tdc`)
:link: ./using_poli/objective_repository/amlodipine_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Amlodipine MPO oracle of GuacaMol.
:::

:::{grid-item-card} Celecoxib rediscovery (using `tdc`)
:link: ./using_poli/objective_repository/celecoxib_rediscovery.html
:columns: 6
The Therapeutics Data Commons' implementation of the Celecoxib rediscovery oracle of GuacaMol.
:::

:::{grid-item-card} Decorator Hop (using `tdc`)
:link: ./using_poli/objective_repository/deco_hop.html
:columns: 6
The Therapeutics Data Commons' implementation of the "deco Hop" oracle of GuacaMol.
:::

:::{grid-item-card} `dockstring` for ligand design
:link: ./using_poli/objective_repository/dockstring.html
:columns: 6
Using `dockstring` to assess the docking score of a small molecule.
:::

:::{grid-item-card} DRD2 docking (using `tdc`)
:link: ./using_poli/objective_repository/albuterol_similarity.html
:columns: 6
The Therapeutics Data Commons' implementation of the DRD2 docking oracle.
:::

:::{grid-item-card} DRD3 (or 3pbl) docking (using `tdc`)
:link: ./using_poli/objective_repository/drd3_docking.html
:columns: 6
A wrapper around the Therapeutics Data Commons implementation of 3pbl docking.
:::

:::{grid-item-card} Fexofenadine MPO (using `tdc`)
:link: ./using_poli/objective_repository/fexofenadine_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Fexofenadine MPO oracle of GuacaMol.
:::

:::{grid-item-card} GSK3β (using `tdc`)
:link: ./using_poli/objective_repository/gsk3_beta.html
:columns: 6
The Therapeutics Data Commons' implementation of the GSK3β oracle.
:::

:::{grid-item-card} Isomer C7H8N2O2 (using `tdc`)
:link: ./using_poli/objective_repository/isomer_c7h8n2o2.html
:columns: 6
The Therapeutics Data Commons' implementation of the first isomer oracle of GuacaMol.
:::

:::{grid-item-card} Isomer C9H10N2O2PF2Cl (using `tdc`)
:link: ./using_poli/objective_repository/isomer_c9h10n2o2pf2cl.html
:columns: 6
The Therapeutics Data Commons' implementation of the second isomer oracle of GuacaMol.
:::

:::{grid-item-card} JNK3 (using `tdc`)
:link: ./using_poli/objective_repository/jnk3.html
:columns: 6
The Therapeutics Data Commons' implementation of the JNK3 oracle.
:::

:::{grid-item-card} Log-solubility (LogP)
:link: ./using_poli/objective_repository/rdkit_logp.html
:columns: 6
Computing the log-quotient of solubilities using `RDKit`.
:::

:::{grid-item-card} Median 1 (using `tdc`)
:link: ./using_poli/objective_repository/median_1.html
:columns: 6
The Therapeutics Data Commons' implementation of the "median 1" oracle of GuacaMol.
:::

:::{grid-item-card} Median 2 (using `tdc`)
:link: ./using_poli/objective_repository/median_2.html
:columns: 6
The Therapeutics Data Commons' implementation of the "median 2" oracle of GuacaMol.
:::

:::{grid-item-card} Mestranol Similarity (using `tdc`)
:link: ./using_poli/objective_repository/albuterol_similarity.html
:columns: 6
The Therapeutics Data Commons' implementation of the Mestranol similarity oracle of GuacaMol.
:::

:::{grid-item-card} Osimetrinib MPO (using `tdc`)
:link: ./using_poli/objective_repository/osimetrinib_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Osimetrinib MPO oracle of GuacaMol.
:::

:::{grid-item-card} Penalized Log-solubility (LogP, using `lambo`)
:link: ./using_poli/objective_repository/penalized_logp_lambo.html
:columns: 6
Computing the penalized log-quotient of solubilities using `lambo`'s implementation.
:::

:::{grid-item-card} Quantitative Estimate of Druglikeness (QED)
:link: ./using_poli/objective_repository/rdkit_qed.html
:columns: 6
Computing the QED using `RDKit`.
:::

:::{grid-item-card} Ranolazine MPO (using `tdc`)
:link: ./using_poli/objective_repository/ranolazine_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Ranolazine MPO oracle of GuacaMol.
:::

:::{grid-item-card} Scaffold Hop (using `tdc`)
:link: ./using_poli/objective_repository/deco_hop.html
:columns: 6
The Therapeutics Data Commons' implementation of the scaffold Hop oracle of GuacaMol.
:::

:::{grid-item-card} Sitagliptin MPO (using `tdc`)
:link: ./using_poli/objective_repository/sitagliptin_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Sitagliptin MPO oracle of GuacaMol.
:::

:::{grid-item-card} Synthetic Accessibility (SA, using `tdc`)
:link: ./using_poli/objective_repository/sa_tdc.html
:columns: 6
A wrapper around the Therapeutics Data Commons implementation of the synthetic accessibility oracle.
:::

:::{grid-item-card} Thiothixene rediscovery (using `tdc`)
:link: ./using_poli/objective_repository/thiothixene_rediscovery.html
:columns: 6
The Therapeutics Data Commons' implementation of the Thiothixene rediscovery oracle of GuacaMol.
:::

:::{grid-item-card} Troglitazone rediscovery (using `tdc`)
:link: ./using_poli/objective_repository/troglitazone_rediscovery.html
:columns: 6
The Therapeutics Data Commons' implementation of the Troglitazone rediscovery oracle of GuacaMol.
:::

:::{grid-item-card} Valsartan SMARTS (using `tdc`)
:link: ./using_poli/objective_repository/valsartan_smarts.html
:columns: 6
The Therapeutics Data Commons' implementation of the Valsartan SMARTS oracle of GuacaMol.
:::

:::{grid-item-card} Zaleplon MPO (using `tdc`)
:link: ./using_poli/objective_repository/zaleplon_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Zaleplon MPO oracle of GuacaMol.
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

### Discrete

::::{grid}
:gutter: 3

:::{grid-item-card} Random Mutations
:link: ./using_poli_baselines/random_mutations.html
:columns: 6
Optimizing a discrete sequence by performing random mutations
:::

:::{grid-item-card} Increasingly high-dimensional combinatorial and continuous embeddings (Bounce) 
:link: ./using_poli_baselines/bounce.html
:columns: 6

Papenmeier et al's Bounce, using their official implementation.
:::

:::{grid-item-card} Bayesian optimization with probabilistic reparametrization (ProbRep) 
:link: ./using_poli_baselines/probrep.html
:columns: 6

Daulton et al's PR, using their official implementation.
:::

::::

### Continuous

::::{grid}
:gutter: 3

:::{grid-item-card} CMA-ES
:link: ./using_poli_baselines/cma_es.html
:columns: 6
An evolutionary strategy for continuous problems
:::

:::{grid-item-card} Line Bayesian Optimization
:link: ./using_poli_baselines/latent_space_bo.html
:columns: 6
A version of Bayesian Optimization where the acquisition is optimized over a line.
:::

:::{grid-item-card} Hvarfner's Vanilla Bayesian Optimization
:link: ./using_poli_baselines/hvarfners_vanilla_bo.html
:columns: 6

Bayesian Optimization with log-expected improvement and a dimensionality-dependent prior over the lengthscales.

:::

:::{grid-item-card} Sparse Axis-Aligned Subspace Bayesian Optimization (SAASBO) 
:link: ./using_poli_baselines/saasbo.html
:columns: 6

Eriksson and Jankowiak's SAASBO, using `Ax`.
:::

:::{grid-item-card} Adaptive expanding subspaces (BAxUS) 
:link: ./using_poli_baselines/baxus.html
:columns: 6

Papenmeier et al's BAxUS, using their official implementation.
:::

::::

## Cite us and other relevant work

If you use certain black boxes, we expect you to cite the relevant work. [Check inside the documentation of each black box for the relevant references](./using_poli/objective_repository/all_objectives.md).

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

