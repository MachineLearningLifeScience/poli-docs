# Documentation for `poli` and `poli-baselines` 🧪

This repository contains a `jupyter-book` with documentation for `poli` and `poli-baselines`

## Building the documentation

The folder `./docs/poli-docs` is a [Jupyter Book](https://jupyterbook.org/en/stable/intro.html). To build it, create a new environment (`python>=3.9`) and install the requirements:

```bash
conda create -n poli-docs python=3.9
conda activate poli-docs
pip install -r requirements.txt
```

## Adding relevant files to the `_toc.yml`

If you're building a new page, it's quite likely you'll have to add a new entry to the relevant section of `_toc.yml`.

## (Maybe) Adding mock dependencies to the `_config.yml`

If you're implementing a new black box, it is likely that some pages won't build in the API if the right dependencies are not installed for `poli`. Add mock dependencies in the `_config.yml` to prevent this.

## Building

After this, you can build the documentation using

```bash
jupyter-book build --all docs/poli-docs
```

## Deployment

Since we are relying on building the website locally (because of `foldx` dependencies), you will need to

1. `pip install ghp-import`
2. run `ghp-import -n -p -f ./docs/poli-docs/_build/html`
