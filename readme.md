# Documentation for `poli` and `poli-baselines` 🧪

This repository contains a `jupyter-book` with documentation for `poli` and `poli-baselines`

## Building the documentation

The folder `./docs/poli-docs` is a [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). To build it, create a new environment (`python>=3.9`) and install the requirements:

```bash
conda create -n poli-docs python=3.9
conda activate poli-docs
pip install -r requirements.txt
```

## Building

After this, you can build the documentation using

```bash
jupyter-book build --all docs/poli-docs
```
