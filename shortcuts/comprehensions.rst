Comprehensions
==============

**Comprehensions condense for loops into a one-line expression.**

List Comprehensions
-------------------

A list comprehension creates a list:

.. code:: python3

   squares = [x ** 2 for x in range(10)]

Produces the same result as:

.. code:: python3

   squares = []
   for x in range(10):
       squares.append(x ** 2)

Conditionals
~~~~~~~~~~~~

The comprehension may contain an ``if`` clause to filter the list:

.. code:: python3

   squares = [x ** 2 for x in range(10) if x % 3 == 0]

Note that you can also place an ``if`` on the other side of the ``for``
as a ternary expression. This leads to a different result:

.. code:: python3

   squares = [x ** 2 if x % 3 == 0 else -1 for x in range(10)]

Nested Comprehensions
~~~~~~~~~~~~~~~~~~~~~

It is perfectly fine to place one comprehension inside another. The
following code creates a 5x5 matrix:

.. code:: python3

   [[x * y for x in range(5)] for y in range(5)]

Note that you can concatenate the ``for`` statements without the extra
brackets. In that case the result is a flat list:

.. code:: python3

   [x * y for x in range(5) for y in range(5)]

The join pattern
~~~~~~~~~~~~~~~~

Comprehensions that produce a list of strings are often found together
with ``join()``, e.g. to format text output:

.. code:: python3

   ';'.join([char.upper() for char in 'abcde'])

----

Dict comprehensions
-------------------

This variant produces dictionaries:

.. code:: python3

   ascii_table = {x: chr(x) for x in range(65, 91)}

----

Set comprehensions
------------------

The same with a set:

.. code:: python3

   unique = {x.upper() for x in 'Hello World'}

----

Generator expressions
---------------------

Finally, you can use a comprehension to define generators:

.. code:: python3

   squares = (x ** 2 for x in range(1_000_000_000_000_000))
   print(next(squares))
