Installing Packages with pip
============================

``pip`` is a tool to install Python packages and resolve dependencies
automatically. This section lists a couple of things you can do with
``pip``:

Install a package
~~~~~~~~~~~~~~~~~

To install a Python package, call ``pip`` with the package name:

::

   pip install pandas

You can specify the exact version of a package:

::

   pip install pandas==0.25.0

--------------

Install many packages
~~~~~~~~~~~~~~~~~~~~~

First, create a file ``requirements.txt`` in your project directory. The
file should look similar to this:

::

   pandas==0.25
   numpy>=1.17
   scikit-learn
   requests

Second, ask ``pip`` to install everything:

::

   pip -r requirements.txt

--------------

Install from a git repo
~~~~~~~~~~~~~~~~~~~~~~~

If a repository has a ``setup.py`` file, you could install directly from
git. This is useful to install branches, forks and other work in
progress:

::

   pip install git+https://github.com/pandas-dev/pandas.git

--------------

Install a package you are developing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When developing, you might want to pip-install a working copy. This
allows you to import your package (e.g. for testing). Changes to the
code directly take effect in the installation.

For the following to work, your project folder needs to have a
``setup.py``:

::

   pip install --editable .

--------------

List all installed packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This one prints all packages you have installed and their versions:

::

   pip freeze

To search for a pacakge, use ``grep``:

::

   pip freeze | grep pandas


Where does pip store its files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usually, packages are stored in the ``site_packages/`` folder. Where
this one is depends on your distribution and your virtual environment.

You might want to check your ``PYTHONPATH`` environment variable. To do
so from Python, use:

.. code:: python3

   import sys

   print(sys.path)

--------------

.. seealso::

   -  The ``conda`` program (part of the Anaconda distribution) is often a viable alternative to pip
   -  You find all installable packages on the `Python Package Index pypi.org <http://pypi.org>`__
