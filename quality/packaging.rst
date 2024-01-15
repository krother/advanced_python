Create a pip-installable Package
================================

Once a python package (a folder with ``.py`` files), you may want to
make it available to other programs – and people. Making your code
pip-installable can be done by adding an extra configuration files
called ``setup.py``.

Assume your project folder contains:

::

   dungeon_explorer/   - module folder you want to import
   tests/              - the test code for pytest
   .git/               - the commit history (managed by git)
   README.md           - documentation
   LICENSE             - legal info
   setup.py            - used by pip (see below)
   .gitignore          - choose one on Github

The Project Folder
------------------

Your project folder should contain a sub-directory with a name in
**lowercase_with_underscores**. This sub-directory is your python
package! Add your own Python files inside this package folder. The
``setup.py`` script will look for the source code there.

The setup.py file
-----------------

**setuptools** is a Python library that builds and installs Python
packages. You may need to install it first:

::

   pip install setuptools

In order to use setuptools, you need a file called ``setup.py`` that
tells the installer what to install. You can use the following
``setup.py`` file as a starting point:

::

   from setuptools import setup
   import os

   def get_readme():
       """returns the contents of the README file"""
       return open(os.path.join(os.path.dirname(__file__), "README.md")).read()

   setup(
      name="dungeon_explorer",              # name used on PyPi
      version="0.0.1",                      # uses *semantic versioning*
      description="a simpl dungeon RPG",   
      long_description=get_readme(),
      author="your_name",
      author_email="your@name.com",
      packages=["dungeon_explorer"],        # the folder with .py modules
      url="https://github.com/...",
      license="MIT",
      classifiers=[
         "Programming Language :: Python :: 3.10",
         "Programming Language :: Python :: 3.11",
         "Programming Language :: Python :: 3.12",
      ]
   )

Copy this code to a ``setup.py`` file in the top-level folder of your
project and save it.

Here is a `video explaining how setup.py
works <https://www.youtube.com/watch?v=S-Le3PWHqZA>`__.

--------------

Install your program
--------------------

When developing a program, the first thing you want to do is to install
your program in development mode. Go to the folder where the
``setup.py`` file is located and run the command:

::

   python setup.py develop

   OR

   pip install --editable .

This makes your project available to the rest of your Python environment
(Python creates a link to your project somewhere in the PYTHONPATH). Now
you should be able to run from any other Python program:

::

   import dungeon_explorer

In other words, you don’t actually need to be in your project folder to
use your program. This is super convenient! You can use your package
from anywhere as if it were an official library, like **numpy** or
**pydantic**. You should also see your package in the output of
``pip list`` or ``pip freeze``.

This method has the advantage that you can still edit your code, and the
next time you import the library again.

**WARNING:** for the re-import to work, you need to restart the Python
interpreter. Just executing the import twice does not work.

--------------

Installation on other machines
------------------------------

If you want to use your library but not edit it (e.g. in a production
environment), you may want to copy it to where Python stores all the
other packages. This can be done with another one-liner.

::

   python setup.py install

   OR

   pip install .

The files are copied to a folder called ``site-packages/`` . The
location of it depends on your operating system and Python distribution.

--------------

Installation from GitHub
------------------------

If you have a ``setup.py``, you can pip-install your package directly
from GitHub:

::

   pip install <github-url>

--------------

Creating a distribution
-----------------------

If you want to package all files of your projects into an archive, you
can do this with:

::

   python setup.py sdist

This creates a ``dist/`` folder with a ``.tar.gz`` file that you can
move around easily.

--------------

Further Reading
---------------

If you would like to upload your program to PyPi, so that anyone can
install it with

::

   pip install dungeon_explorer

you need to follow a few more steps. This is not difficult but a bit
tedious. We recommend the official
``Packaging Python Projects Tutorial <https://packaging.python.org/tutorials/packaging-projects/>``\ \__.

.. topic:: Authors

   This guide was written together with Paul Wlodkowski and Malte Bonart.
