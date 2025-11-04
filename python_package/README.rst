
Building a Python Package
=========================


In this exercise, you will use  `uv <https://docs.astral.sh/uv/>`__ to create a package structure for the space game.
**uv** is a modern tool for managing virtual environments written in rust. It works similar to **pipenv** and **poetry** but is 100x faster when resolving dependencies.

Exercise 1: Installation
------------------------
Install uv with:

::

    python -m pip install uv

or

::

    curl -LsSf https://astral.sh/uv/install.sh | sh


Exercise 2: Create environment
------------------------------

Create a project folder and execute the commands

::

    uv python install 3.12
    uv init

Check which files have been created.

Exercise 3: pyproject.toml
--------------------------

Download the file :download:`pyproject.toml`

It contains instructions to install and package a Python project.
Inspect the file and clarify its contents.

The file has been written for a different game - modify what is necessary.

Exercise 4: Install libraries
-----------------------------

Install the dependencies listed in `pyproject.toml`:

::

    uv lock
    uv sync

The development libraries are installed by default.

You should see a `venv/` folder that contains the installed libraries.

Exercise 5: Add source code
---------------------------

Add a folder `space_game/` below the folder containing `pyproject.toml`
Place the file `space_game.py` there.

Also create a folder `tests/` that we will use later.

Exercise 6: Execute code
------------------------

Now the program is ready to be executed:

::

    uv run space_game/space_game.py

Or create a file `space_game/__main__.py` and run the python package name:

::

    uv run space_game

In all three cases, the game should start.


Exercise 7: Release the package
-------------------------------

Create a distribution with:

::

    uv build

You should find the release files in the `dist/` folder.

If you want to release the sources only, use:

::

    uv build --sdist
