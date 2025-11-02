Operator Overloading
====================

Python has a long list of special **double-underscore methods** ("dunder methods" or  ``__magic_methods__()``).
All these ``__magic_methods__()`` have a special function and should never be called directly. 
Most of them directly map to Python operators or builtin functions.
Here are some examples:

============== =================================================
method         description
============== =================================================
``__init__()`` called when creating an object from a class
``__repr__()`` called when converting object to a string
``__add__()``  called when using the ``+`` operator on an object
``__mul__()``  called when using the ``*`` operator on an object
``__gt__()``   called when comparing the object to another
``__len__()``  called when using ``len()``
``__hash__()`` called when using the object as a dictionary key
============== =================================================

Common use cases
----------------

I recommend using operator overloading sparingly.
Most of the time, a regular method is easier to read.
Below you find a few examples that I have found useful:

* making objects printable with `__repr__()`  and `__str__()`
* checking equality with `__eq__()`
* making objects sortable with `__lt__()` (less than) or `__gt__()`


Making classes printable
------------------------

One disadvantage of classes is that when you print an object, you will
see something like this:

::

   <__main__.MyClass at 0x7f64519d8438>

A good workaround is to add a special method, ``__repr__(self)`` to the
class that returns a string. This method will be called every time a
string representation is needed: when printing and object, when an
object appears inside a list or in error messages.

Typically, you would build a short string in ``__repr__(self)`` that
describes the object:

.. code:: python3

       def __repr__(self):
           return f"<account of '{self.name}' with {self.balance} galactic credits>"

With this method defined, the instruction

.. code:: python3

   print(a)

Gives a clean summary of the instance.
It is a good idea to implement ``__repr__(self)`` as the first method in any new class.


Sortable Objects
----------------

The method ``__lt__(self, other)`` is implicitly called when comparing
two objects, as done by any sorting algorithm.

.. literalinclude:: sortable_objects.py


Hashable Vectors
----------------

This is a 2D vector class I used for screen positions in a game.
I wanted the vectors to be capable of simple arithmetics. They also needed
to be hashable (which NumPy arrays are not).

.. literalinclude:: vector.py


Dynamic Attributes
------------------

The special methods `__getattr__` and `__setattr__` allow you to intercept the process of attribute access. They work like a more generic **property**. You can use them to retrieve attributes from elsewhere or to generate them on-the-fly. However, since methods use the same mechanism you will always want to call the inherited method.

Execute the example in :download:`getattr_setattr.py`.

Slots
-----

The `__slots__` attribute is a mechanism to define the available attributes more strictly.
This mechanism is used by **dataclasses** and **pydantic** with a more comfortable interface.

Run the example in :download:`slots.py`. 
Remove the comment and run the code again.


Caveats
-------

It is often questionable, whether overloading operators is a good idea.
Many times it is not, because it obscures what is happening behind the scenes.

Compare the clarity of e.g. multiplying matrices with:

.. code:: python3

   T = M1 @ M2

versus

.. code:: python3

   T = np.matmul(M1, M2)

My personal opinion is that, with few exceptions, operator operator_overloading should be used sparingly.
