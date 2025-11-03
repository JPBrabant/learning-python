# `uv`

## TODO
- Installing uv
- Installing Python with uv

## Using uv

Installing Python

    uv python install --default # Install globaly
    uv python upgrade           # Update python
    uv python list              # List all available python version

Starting a new project

    uv init

Adding dependencies

    uv add numpy pandas scikit-learn

Adding dev dependencies

    uv add --dev ruff

Downloading all dependencies

    uv sync

Seeing the depencies tree

    uv tree

Running a script

    uv run main.py


## Using uvx

Allow you to run tools. Equivalent to `uv run`.

Running IPython with pandas and pyarrow to look at a parquet file

    uvx --with pandas,pyarrow ipython

Jupyter lab

    uvx --from jupyter-core --with jupyter jupyter lab

Jupyter notebook

    uvx --from jupyter-core --with jupyter jupyter notebook

ML template 

    uvx --from cookiecutter-data-science ccds