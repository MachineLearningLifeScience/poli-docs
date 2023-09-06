# Protein optimization using `poli`

This book contains documentation on how to use `poli` and `poli-baselines`, our tools for creating and optimizing black box objective functions.

At its core, `poli` allows you to isolate calls to complicated objective functions which might, for example, depend on simulators, binaries, or a weird version of the Java runtime.
Our promise is: if you can run your objective function reliably in a `conda` environment, then you can register it and call it from other projects without having to worry about re-installing all the dependencies.

`poli` comes batteries-included. By this, we mean that there are already a collection of black box objective functions you could register and use out-of-the-box.

## Black-box objective functions

These are some objective functions available on `poli`. **For a full list**, [check here](./using_poli/objective_repository/all_objectives.md).


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

:::{grid-item-card} Protein Stability (using `RaSP`) [WIP]
:link: ./using_poli/objective_repository/RaSP.html
:columns: 6
Rapid Stability Predictions of single mutations from a wildtype. [WIP]
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

:::{grid-item-card} NSGA-2
:link: ./using_poli_baselines/nsga_2.html
:columns: 6
A Genetic algorithm for optimizing more than one metric [WIP]
:::

:::{grid-item-card} CMA-ES
:link: ./using_poli_baselines/cma_es.html
:columns: 6
An evolutionary strategy for continuous problems [WIP]
:::

:::{grid-item-card} Latent Space Bayesian Optimization
:link: ./using_poli_baselines/latent_space_bo.html
:columns: 6
Learning continuous representations and optimizing in latent space. [WIP]
:::

:::{grid-item-card} Graph GA
:link: ./using_poli_baselines/graph_ga.html
:columns: 6
Graph Genetic Algorithms for small molecules. [WIP]
:::

::::

## Get started!

A good place to start is the next chapter! [Go to Getting Started](./getting_started/getting_started.md).


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

