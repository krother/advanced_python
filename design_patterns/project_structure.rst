
Project Structure
=================

To manage dependencies in the project, use the tool **poetry**.

First, install it with:

::

   pip install poetry

Second, copy the file :download:`pyproject.toml` into the folder with the prototype code.
The file already contains the section required for poetry.

File Structure
--------------

You may have to move some files around to run the prototype with **poetry**.
Here is a working file structure:

::

   ├── dungeon_explorer
   │   ├── game.py
   │   ├── main.py
   │   └── tiles
   │       ├── armor.png
   │       ├── ART_LICENSE.txt
   │       ├── bat.png
   │       ├── ...
   │       └── water.png
   ├── pyproject.toml
   ├── README.md
   └── requirements.txt


Install Dependencies
--------------------

Use **poetry** to install all required libraries with:

::

   poetry lock
   poetry install

This should create a virtual environment and install all dependencies.

If you have a different Python version and the dependencies cannot be installed,
you may want to replace some of the version numbers in `pyproject.toml` by `"*"` and try again.

.. warning::

   OpenCV requires a binary component that should be installed by the Python package manger.
   However, if it fails, please refer to the `OpenCV documentation <https://pypi.org/project/opencv-python/>`__

Run the Game through poetry
---------------------------

Try

::

    poetry run python dungeon_explorer/main.py

or

::
    
    poetry shell
    
    python dungeon_explorer/main.py
