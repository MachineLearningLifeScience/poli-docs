# Documentation on protein optimization

This repository contains documentation on how protein optimization is currently being pursued, at least in the context of black-box optimization.

## Building the documentation


The folder `./docs/protein-optimization` is a [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). To build it, create a new environment (`python>=3.9`) and install the requirements:

```bash
pip install jupyter-book biopython pandas git+https://github.com/miguelgondu/poli.git 
```

## Installing poli baselines

At the time of writing, `poli-baselines` is a private repository. This means that you'll have to install it by hand. Start by cloning:

```bash
git clone git@github.com:MachineLearningLifeScience/poli-baselines.git
cd ./poli-baselines
pip install -e .
```

## Building

After this, you can build the documentation using

```bash
jupyter-book build --all docs/protein-optimization
```

