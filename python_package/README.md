
# Build a Python Package

In this exercise, you will use  `uv <https://docs.astral.sh/uv/>`__ to create a package structure for the game `pac` application.
**uv** is a modern tool for managing virtual environments written in rust. It works similar to **pipenv** and **poetry** but is 100x faster when resolving dependencies.

## 1. Installation

Install uv with:

    python -m pip install uv

or

    curl -LsSf https://astral.sh/uv/install.sh | sh


## 2. Create environment

Create a project folder and execute the commands

    uv python install 3.12
    uv init

Check what files have been created.

## 3. pyproject.toml

Download the file [pyproject.toml](pyproject.toml).
It contains instructions to install and package the project.
Inspect the file and clarify its contents.

## 4. Install libraries

Install the dependencies listed in `pyproject.toml`:

    uv lock
    uv sync

The development libraries are installed by default.

You should see a `venv/` folder that contains the installed libraries.

## 5. Add source code

Add a folder `pac/` below the folder containing `pyproject.toml`
Download and add the following two files:

* [pac_game.py](pac_game.py)
* [tiles.png](tiles.png)

Also create a folder `tests/` that we will use later.

## 6. Execute code

Now the program is ready to be executed:

    uv run pac/pac_game.py

Also can also use the configuration in `[project.scripts]`:

    uv run pacm

Or use the file [__main__.py](__main__.py) and run the python package name:

    uv run pac

In all three cases, you should see a graphical window with some starter setup pop up.


## 7. Release the package

Create a distribution with:

    uv build

You should find the release files in the `dist/` folder.

If you want to release the sources only, use:

    uv build --sdist

## 8. Install the package

The newly created package can be installed with ``pip`` from the release wheel:

    pip install dist/pac-1.1.0-py3-none-any.whl

and

    python
    
    >>> import pac
