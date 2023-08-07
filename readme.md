# Documentation on protein optimization

This repository contains documentation on how protein optimization is currently being pursued, at least in the context of black-box optimization.

## Building the documentation

The folder `./docs/protein-optimization` is a [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). To build it, create a new environment (`python>=3.9`) and install the requirements:

```bash
pip install jupyter-book biopython pandas
```

After this, you can build the documentation using

```bash
jupyter-book build --all docs/protein-optimization
```

