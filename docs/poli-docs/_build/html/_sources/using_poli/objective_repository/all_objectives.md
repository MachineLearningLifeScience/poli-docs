# All objective functions

These are all the objective functions available on `poli`. Click on one of them to get a minimal working example of how to use it.


## Toy problems

::::{grid}
:gutter: 3

:::{grid-item-card} Aloha
:link: ./aloha.html
:columns: 6
A toy example about optimizing 5-letter words to spell "ALOHA"
:::

:::{grid-item-card} Toy continuous problems
:link: ./toy_continuous_problems.html
:columns: 6
The usual benchmark functions for continuous optimization (e.g. `easom`, or `ackley_function_01`)
:::

:::{grid-item-card} White noise
:link: ./white_noise.html
:columns: 6
White noise drawn from a unit Gaussian
:::

::::

## Small molecules

Most of our problems are based on the [PMO](https://github.com/wenhao-gao/mol_opt) benchmark, by Gao et al {cite:p}`Gao:PMO:2022`, which extends the GuacaMol Benchmark proposed by Brown et al {cite:p}`Brown:guacamol:2019`.

::::{grid}
:gutter: 3

:::{grid-item-card} Albuterol Similarity (using `tdc`)
:link: ./albuterol_similarity.html
:columns: 6
The Therapeutics Data Commons' implementation of the Albuterol similarity oracle of GuacaMol.
:::

:::{grid-item-card} Amlodipine MPO (using `tdc`)
:link: ./amlodipine_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Amlodipine MPO oracle of GuacaMol.
:::

:::{grid-item-card} Celecoxib rediscovery (using `tdc`)
:link: ./celecoxib_rediscovery.html
:columns: 6
The Therapeutics Data Commons' implementation of the Celecoxib rediscovery oracle of GuacaMol.
:::

:::{grid-item-card} Decorator Hop (using `tdc`)
:link: ./deco_hop.html
:columns: 6
The Therapeutics Data Commons' implementation of the "deco Hop" oracle of GuacaMol.
:::

:::{grid-item-card} `dockstring` for ligand design
:link: ./dockstring.html
:columns: 6
Using `dockstring` to assess the docking score of a small molecule.
:::

:::{grid-item-card} DRD2 docking (using `tdc`)
:link: ./albuterol_similarity.html
:columns: 6
The Therapeutics Data Commons' implementation of the DRD2 docking oracle.
:::

:::{grid-item-card} DRD3 (or 3pbl) docking (using `tdc`)
:link: ./drd3_docking.html
:columns: 6
A wrapper around the Therapeutics Data Commons implementation of 3pbl docking.
:::

:::{grid-item-card} Fexofenadine MPO (using `tdc`)
:link: ./fexofenadine_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Fexofenadine MPO oracle of GuacaMol.
:::

:::{grid-item-card} GSK3β (using `tdc`)
:link: ./gsk3_beta.html
:columns: 6
The Therapeutics Data Commons' implementation of the GSK3β oracle.
:::

:::{grid-item-card} Isomer C7H8N2O2 (using `tdc`)
:link: ./isomer_c7h8n2o2.html
:columns: 6
The Therapeutics Data Commons' implementation of the first isomer oracle of GuacaMol.
:::

:::{grid-item-card} Isomer C9H10N2O2PF2Cl (using `tdc`)
:link: ./isomer_c9h10n2o2pf2cl.html
:columns: 6
The Therapeutics Data Commons' implementation of the second isomer oracle of GuacaMol.
:::

:::{grid-item-card} JNK3 (using `tdc`)
:link: ./jnk3.html
:columns: 6
The Therapeutics Data Commons' implementation of the JNK3 oracle.
:::

:::{grid-item-card} Log-solubility (LogP)
:link: ./rdkit_logp.html
:columns: 6
Computing the log-quotient of solubilities using `RDKit`.
:::

:::{grid-item-card} Median 1 (using `tdc`)
:link: ./median_1.html
:columns: 6
The Therapeutics Data Commons' implementation of the "median 1" oracle of GuacaMol.
:::

:::{grid-item-card} Median 2 (using `tdc`)
:link: ./median_2.html
:columns: 6
The Therapeutics Data Commons' implementation of the "median 2" oracle of GuacaMol.
:::

:::{grid-item-card} Mestranol Similarity (using `tdc`)
:link: ./albuterol_similarity.html
:columns: 6
The Therapeutics Data Commons' implementation of the Mestranol similarity oracle of GuacaMol.
:::


:::{grid-item-card} Osimetrinib MPO (using `tdc`)
:link: ./osimetrinib_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Osimetrinib MPO oracle of GuacaMol.
:::

:::{grid-item-card} Penalized Log-solubility (LogP, using `lambo`)
:link: ./penalized_logp_lambo.html
:columns: 6
Computing the penalized log-quotient of solubilities using `lambo`'s implementation.
:::

:::{grid-item-card} Ranolazine MPO (using `tdc`)
:link: ./ranolazine_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Ranolazine MPO oracle of GuacaMol.
:::

:::{grid-item-card} Scaffold Hop (using `tdc`)
:link: ./deco_hop.html
:columns: 6
The Therapeutics Data Commons' implementation of the scaffold Hop oracle of GuacaMol.
:::

:::{grid-item-card} Sitagliptin MPO (using `tdc`)
:link: ./sitagliptin_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Sitagliptin MPO oracle of GuacaMol.
:::

:::{grid-item-card} Synthetic Accessibility (SA, using `tdc`)
:link: ./sa_tdc.html
:columns: 6
A wrapper around the Therapeutics Data Commons implementation of the synthetic accessibility oracle.
:::

:::{grid-item-card} Thiothixene rediscovery (using `tdc`)
:link: ./thiothixene_rediscovery.html
:columns: 6
The Therapeutics Data Commons' implementation of the Thiothixene rediscovery oracle of GuacaMol.
:::

:::{grid-item-card} Troglitazone rediscovery (using `tdc`)
:link: ./troglitazone_rediscovery.html
:columns: 6
The Therapeutics Data Commons' implementation of the Troglitazone rediscovery oracle of GuacaMol.
:::

:::{grid-item-card} Valsartan SMARTS (using `tdc`)
:link: ./valsartan_smarts.html
:columns: 6
The Therapeutics Data Commons' implementation of the Valsartan SMARTS oracle of GuacaMol.
:::

:::{grid-item-card} Quantitative Estimate of Druglikeness (QED)
:link: ./rdkit_qed.html
:columns: 6
Computing the QED using `RDKit`.
:::

:::{grid-item-card} Zaleplon MPO (using `tdc`)
:link: ./zaleplon_mpo.html
:columns: 6
The Therapeutics Data Commons' implementation of the Zaleplon MPO oracle of GuacaMol.
:::

::::

## Proteins

::::{grid}
:gutter: 3

:::{grid-item-card} Protein SASA score (using `foldx`)
:link: ./foldx_sasa.html
:columns: 6
Solvent accessibility of mutations of a wildtype using `foldx`
:::

:::{grid-item-card} Protein Stability (using `foldx`)
:link: ./foldx_stability.html
:columns: 6
Stability of mutations of a wildtype using `foldx`
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

## Other

::::{grid}
:gutter: 3

:::{grid-item-card} Mario jumps
:link: ./super_mario_bros.html
:columns: 6
Optimizing the number of jumps on a Super Mario Bros level
:::
