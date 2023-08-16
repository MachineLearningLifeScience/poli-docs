# Tutorials on protein optimization using poli

This book contains documentation on how to use `poli` and `poli-baselines`, our tools for creating and optimizing black box objective functions.

At its core, `poli` allows you to isolate calls to complicated objective functions which might, for example, depend on simulators, binaries, or a weird version of the Java runtime.
Our promise is: if you can run your objective function reliably in a `conda` environment, then you can register it and call it from other projects without having to worry about re-installing all the dependencies.

`poli` comes batteries-included. By this, we mean that there are already a collection of black box objective functions you could register and use out-of-the-box. Examples include:
- standard white noise,
- computing the stability of proteins and their mutations from a wildtype `pdb`,
- optimizing the number of jumps Mario performs in a Super Mario Bros level sampled from the latent space of a Variational Autoencoder.
- optimizing the QED and penalized logP of small molecules, presented as either SELFIES or SMILES. [WIP]

On top of `poli`, we provide `poli-baselines`, a collection of black-box optimization algorithms (focusing especially on *discrete* sequences). Examples include
- Random mutations,
- Evolutionary and genetic algorithms like CMA-ES, or NSGA-2 [WIP],
- Bayesian Optimization in latent space [WIP].

A good place to start is the next chapter! [Go to Getting Started](./getting_started/getting_started.md).

## Contents

```{tableofcontents}
```