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

----


Recap: Number Comprehensions
----------------------------

Create the following data with one-liners:

.. code:: python3

    # 1. integers
    a = ...
    assert a == [1, 2, 3, 4, 5, 6]

    # 2. squares
    a = ...
    assert a == [1, 4, 9, 16, 25, 36]

    # 3. fractions
    a = ...
    assert a == [1.0, 0.5, 0.33, 0.25, 0.2, 0.17, 0.14]

    # 4. filtering
    a = range(100)
    b = ... a ...
    assert b == [11, 22, 33, 44, 55, 66, 77, 88, 99]

    # 5. dictionary of squares
    a = ...
    assert a == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

    # 6. split
    b = ...
    assert b == [[1, 2], [3, 4], [5, 6]]

    # 7. concatenate
    c = ... b ...
    assert c == [1, 2, 3, 4, 5, 6]
