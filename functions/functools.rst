Map-Filter-Reduce
=================

Python offers many functions that can be used to implement patterns from
*functional programming*.

**Functional Programming** is a programming philosophy where a program
is defined by functions. These functions are stateless (i.e. there are
no global variables). This paradigm helps designing distributed and
concurrent algorithms.

Although one would rarely implement these in pure Python, it is a good
exercise. Functional code often comes out very clean and is easy to
debug and maintain.

A side effect is that it helps you to avoid class-based implementations,
which often are more wordy.

----

Map
---

The ``map()`` function applies a function to all elements of an
iterable. It is returning a generator. ``map()`` is an alternative to a
comprehension.

.. code:: python3

   def square(x):
       return x ** 2

   squares = map(square, numbers)
   print(squares)
   print(list(squares))

--------------

Filter
------

The ``filter()`` function returns all elements of an iterable for which
a function returns ``True``. It is the functional equivalent of the
``if`` clause in a comprehension.

.. code:: python3

   def odd(x):
       return x % 2 != 0

   odd_numbers = filter(odd, range(10))
   print(odd_numbers)
   print(list(odd_numbers))

--------------

Reduce
------

The ``reduce`` function aggregates data by recursively calling the same
function. For instance, you could use it to add numbers and concatenate
lists:

.. code:: python3

   from functools import reduce

   numbers = [1, 2, 3, 4, 5, 6, 7, 8]


   def add(x, y):
       return x + y

   print(reduce(add, numbers))
   print(reduce(add, [[1, 2, 3], [4, 5, 6]]))

``reduce`` allows for quite sophisticated patterns:

.. code:: python3

   from functools import reduce

   words = [
       (455, 'sea'),
       (336, 'boat'),
       (281, 'white'),
       (1226, 'whale'),
       (329, 'captain'),
       (510, 'Ahab')
   ]


   def newlines(a, b):
       return a + '\n' + b


   def wordformat(x):
       number, word = x
       return f"{word:>10s}:{number:5}"


   print(reduce(newlines, map(wordformat, words)))

--------------

Partial
-------

The ``functools`` module contains a couple of ways to manipulate
functions. One of them is ``partial`` that fills in a part of the
parameters, resulting in a new function:

.. code:: python3

   from functools import partial

   add3 = partial(add, 3)   # add3 is a function
   print(add3(5))           # results in 8

   add5 = partial(add, 5)   # can be done more than once
   print(add5(8))           # results in 13
