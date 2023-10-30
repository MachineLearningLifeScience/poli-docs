# All objective functions

These are all the objective functions available on `poli`. Click on one of them to get a minimal working example of how to use it.


### Toy problems

::::{grid}
:gutter: 3

:::{grid-item-card} White noise
:link: ./white_noise.html
:columns: 6
White noise drawn from a unit Gaussian
:::

:::{grid-item-card} Aloha
:link: ./aloha.html
:columns: 6
A toy example about optimizing 5-letter words to spell "ALOHA"
:::

::::

### Small molecules

Most of our problems are based on the [PMO]() benchmark, by Gao et al [TODO: add cite].

::::{grid}
:gutter: 3

:::{grid-item-card} Quantitative Estimate of Druglikeness (QED)
:link: ./rdkit_qed.html
:columns: 6
Computing the QED using `RDKit`.
:::

:::{grid-item-card} Log-solubility (LogP)
:link: ./rdkit_logp.html
:columns: 6
Computing the log-quotient of solubilities using `RDKit`.
:::

:::{grid-item-card} Penalized Log-solubility (LogP, using `lambo`)
:link: ./penalized_logp_lambo.html
:columns: 6
Computing the penalized log-quotient of solubilities using `lambo`'s implementation.
:::

:::{grid-item-card} DDR3 (or 3pbl) docking (using `tdc`)
:link: ./ddr3_docking.html
:columns: 6
A wrapper around the Therapeutics Data Commons implmenetation of 3pbl docking.
:::

:::{grid-item-card} Synthetic Accessibility (SA, using `tdc`)
:link: ./sa_tdc.html
:columns: 6
A wrapper around the Therapeutics Data Commons implmenetation of the synthetic accessibility oracle.
:::

:::{grid-item-card} TDC oracles [WIP]
:link: ./tdc_oracles.html
:columns: 6
Some of the oracles provided by the Therapeutics Data Commons. [WIP]
:::

:::{grid-item-card} GuacaMol [WIP]
:link: ./tdc_oracles.html
:columns: 6
Some of the oracles provided by GuacaMol. [WIP]
:::

::::

### Proteins

::::{grid}
:gutter: 3

:::{grid-item-card} Protein Stability (using `foldx`)
:link: ./foldx_stability.html
:columns: 6
Stability of mutations of a wildtype using `foldx`
:::

:::{grid-item-card} Protein SASA score (using `foldx`)
:link: ./foldx_sasa.html
:columns: 6
Solvent accessibility of mutations of a wildtype using `foldx`
:::

:::{grid-item-card} Protein Stability (using `RaSP`)
:link: ./RaSP.html
:columns: 6
Rapid Stability Predictions of single mutations from a wildtype.
:::

:::{grid-item-card} RFP Fluorescence Protein Stability (using `lambo`)
:link: ./foldx_rfp_lambo.html
:columns: 6
LaMBO Fluorescence (RFP) by stability and solvent-accessible surface area.
:::

::::

### Other

::::{grid}
:gutter: 3

:::{grid-item-card} Mario jumps
:link: ./super_mario_bros.html
:columns: 6
Optimizing the number of jumps on a Super Mario Bros level
:::
