Modules
=======

Any Python file (ending with ``.py``) can be imported by Python script.
A single Python file is also called a **module**. This helps you to
divide a bigger program into several smaller pieces.

For instance if you have a file ``names.py`` containing the following:

.. code:: python3

   FIRST_NAMES = ['Alice', 'Bob', 'Charlie']

Then you can write (e.g. in a second Python file in the same directory):

.. code:: python3

   import names
   print(names.FIRST_NAMES)

----

Packages
========

For big programs, it is useful to divide up the code among several
directories. A directory from which you import Python modules is called a **package**.
For instance, you could have the following files in a package ``namedata``:

::

   namedata/
       __init__.py
       names.py

----

Importing modules and packages
------------------------------

To import from a module, a package or their contents, place its name
(without .py) needs to be given in the import statement. Import
statements can look like this:

.. code:: python3

   import names
   import names as n
   from names import FIRST_NAMES
   from namedata.names import FIRST_NAMES

It is strongly recommended to list the imported variables and functions
explicitly and not write

.. code:: python3

   from names import *

The latter makes debugging difficult.

When importing, Python generates intermediate files (bytecode) in the
``__pycache__`` directory that help to execute programs more
efficiently. It is managed automatically, and you can safely ignore it.

----

The __init__ file
-----------------

You can define the file ``__init__.py`` to make importing from packages more flexible.
It is executed automatically when you import anything from that package.
Suppose you want to use an object from a package, you would import it with:

.. code:: python3

   from namedata.names import FIRST_NAMES

Now you create a ``__init__.py`` file with a single line:

.. code:: python3

   from names import FIRST_NAMES

That import is made available in the namespace of the package, so that the following works:

.. code:: python3

   from namedata import FIRST_NAMES


The ``__init__.py`` file makes is easier to move objects around inside a package.

----

How does Python find modules and packages?
------------------------------------------

When importing modules or packages, Python needs to know where to find
them. There is a certain sequence of directories in which Python looks
for things to import:

-  The current directory.
-  The site-packages folder (where Python is installed).
-  In directories in the ``PYTHONPATH`` environment variable.

You can see all directories from within Python by checking the ``sys.path`` variable:

.. code:: python3

   import sys
   print sys.path
