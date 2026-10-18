# anysolv-tutorial

<!-- badges -->
[![CI](https://github.com/yu9824/anysolv-tutorial/actions/workflows/CI.yml/badge.svg)](https://github.com/yu9824/anysolv-tutorial/actions/workflows/CI.yml)
[![docs](https://github.com/yu9824/anysolv-tutorial/actions/workflows/docs.yml/badge.svg)](https://github.com/yu9824/anysolv-tutorial/actions/workflows/docs.yml)
[![release-pypi](https://github.com/yu9824/anysolv-tutorial/actions/workflows/release.yml/badge.svg)](https://github.com/yu9824/anysolv-tutorial/actions/workflows/release.yml)

<!--
[![python_badge](https://img.shields.io/pypi/pyversions/anysolv-tutorial)](https://pypi.org/project/anysolv-tutorial/)
[![license_badge](https://img.shields.io/pypi/l/anysolv-tutorial)](https://pypi.org/project/anysolv-tutorial/)
[![PyPI version](https://badge.fury.io/py/anysolv-tutorial.svg)](https://pypi.org/project/anysolv-tutorial/)
[![Downloads](https://static.pepy.tech/badge/anysolv-tutorial)](https://pepy.tech/project/anysolv-tutorial)

[![Conda Version](https://img.shields.io/conda/vn/conda-forge/anysolv-tutorial.svg)](https://anaconda.org/conda-forge/anysolv-tutorial)
[![Conda Platforms](https://img.shields.io/conda/pn/conda-forge/anysolv-tutorial.svg)](https://anaconda.org/conda-forge/anysolv-tutorial)
-->

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://github.com/python/mypy)
<!-- /badges -->

## Using this as a template

Bulk-replace the project name, set up ssh-agent on the host, etc.

## Installation

```bash
# standard
pip install git+https://github.com/yu9824/anysolv-tutorial.git

# with Cython compiling
pip install git+https://github.com/yu9824/anysolv-tutorial.git#subdirectory=packages/setuptools/cython

```

### Docker

```bash
git clone https://github.com/yu9824/anysolv-tutorial.git
cd anysolv-tutorial
docker build -f docker/Dockerfile -t anysolv-tutorial .
docker run --rm -it anysolv-tutorial
```

The image contains the package with its optional dependencies and starts a Python shell. The development container lives in `.devcontainer/` instead.

## Directory layout

| Directory | Purpose |
| --- | --- |
| `src/anysolv_tutorial/` | Package source |
| `tests/` | pytest tests |
| `notebooks/` | Notebooks for experimentation (paired with `.py` via jupytext) |
| `data/raw/` | Raw, as-obtained data. Contents are not tracked |
| `data/processed/` | Preprocessed data. Contents are not tracked |
| `models/` | Trained models. Contents are not tracked |
| `docs_src/` | Sphinx source |
| `packages/` | Package templates for different build configurations |
| `examples/` | Example scripts |
| `docker/` | Docker image for users of the package |
| `.devcontainer/` | Development container (VS Code Dev Containers) |
