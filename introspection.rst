Introspection
=============

Introspection is a feature of Python by which you can examine objects
(including variables, functions, classes, modules) inside a running
Python environment (a program or shell session).

Exploring the namespace
-----------------------

In Python all objects (variables, modules, classes, functions and your
main program) are boxes called **namespaces**. You can imagine the
namespace of an object as the data and functions inside than object. You
can explore a namespace with the ``dir()`` function.

Exploring the namespace of a variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With a string object, you see all the string methods:


.. code:: python3

   s = "Emily"
   print(dir(s))

Exploring the namespace of a module:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The same works for a module you import:


.. code:: python3

   import time
   print(dir(time))

Listing the builtin functions:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You also can view all builtin functions:


.. code:: python3

   print(dir(__builtins__))

The help function
-----------------

You can get context-sensitive help to functions, methods and classes
with ``help()`` function.


.. code:: python3

   import time
   print help(time.asctime)

``help()`` utilizes the triple-quoted comments called **docstrings**, so
that documentation you write for your own functions is also availabel
through ``help()``:

Everything is an object
-----------------------

One consequence of the dynamic typing is that Python can treat
everything it manages technically in the same way. **Everything is an
object** is a common phrase describing how Python works. There is no
fundamental difference between a function and an integer. Many advanced
features of Python are built on this concept.
