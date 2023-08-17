# Protein optimization using `poli`

This book contains documentation on how to use `poli` and `poli-baselines`, our tools for creating and optimizing black box objective functions.

At its core, `poli` allows you to isolate calls to complicated objective functions which might, for example, depend on simulators, binaries, or a weird version of the Java runtime.
Our promise is: if you can run your objective function reliably in a `conda` environment, then you can register it and call it from other projects without having to worry about re-installing all the dependencies.

`poli` comes batteries-included. By this, we mean that there are already a collection of black box objective functions you could register and use out-of-the-box.

## Black-box objective functions

These are some objective functions available on `poli`. **For a full list**, check [getting started](./getting_started/getting_started.md).

::::{grid}
:gutter: 3

:::{grid-item-card} White noise
:link: ./using_poli/objective_repository/white_noise.html
:columns: 4
White noise drawn from a unit Gaussian
:::

:::{grid-item-card} Aloha
:link: ./using_poli/objective_repository/aloha.html
:columns: 4
A toy example about optimizing 5-letter words to spell "ALOHA"
:::

:::{grid-item-card} Protein Stability
:link: ./using_poli/objective_repository/foldx_stability.html
:columns: 4
Stability of mutations of a wildtype using `foldx`
:::

:::{grid-item-card} Mario jumps
:link: ./using_poli/objective_repository/super_mario_bros.html
:columns: 4
Optimizing the number of jumps on a Super Mario Bros level
:::

:::{grid-item-card} Small molecule properties
:link: ./using_poli/objective_repository/small_molecule.html
:columns: 4
Small molecule's synthesizability, druglikeness, and more. [WIP]
:::

:::{grid-item-card} RaSP
:link: ./using_poli/objective_repository/RaSP.html
:columns: 4
Rapid Stability Predictions of single mutations from a wildtype. [WIP]
:::

:::{grid-item-card} TDC oracles
:link: ./using_poli/objective_repository/tdc_oracles.html
:columns: 4
Some of the oracles provided by the Therapeutics Data Commons. [WIP]
:::

::::
## Black-box optimization algorithms

On top of `poli`, we provide `poli-baselines`, a collection of **black-box optimization algorithms** (focusing especially on *discrete* sequences). Examples include

::::{grid}
:gutter: 3

:::{grid-item-card} Random Mutations
:link: ./using_poli_baselines/random_mutations.html
:columns: 4
Optimizing a discrete sequence by performing random mutations
:::

:::{grid-item-card} NSGA-2
:link: ./using_poli_baselines/nsga_2.html
:columns: 4
A Genetic algorithm for optimizing more than one metric [WIP]
:::

:::{grid-item-card} CMA-ES
:link: ./using_poli_baselines/cma_es.html
:columns: 4
An evolutionary strategy for continuous problems [WIP]
:::

:::{grid-item-card} Latent Space Bayesian Optimization
:link: ./using_poli_baselines/latent_space_bo.html
:columns: 4
Learning continuous representations and optimizing in latent space. [WIP]
:::

:::{grid-item-card} Graph GA
:link: ./using_poli_baselines/graph_ga.html
:columns: 4
Graph Genetic Algorithms for small molecules. [WIP]
:::

::::

## Get started!

A good place to start is the next chapter! [Go to Getting Started](./getting_started/getting_started.md).

<!-- ## Contents of the book

```{tableofcontents}
``` -->

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
