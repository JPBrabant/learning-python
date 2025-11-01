# `uv`

## TODO
- Installing uv
- Installing Python with uv

## Using uv

Starting a new project

    uv init

Adding dependencies

    uv add pandas

Adding dev dependencies

    uv add --dev ...

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