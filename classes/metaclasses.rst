Metaclasses
===========

Metaclasses change the objects creation mechanics in Python.

The when Python creates an object, it calls the ``__new__()`` method of
the metaclass. The default behavior of ``__new__()`` is that it creates
an instance and calls its ``__init__()``. Now you could write a new
metaclass that instead of calling ``__init__()`` does something else.

Valid Use Cases for changing a metaclass are:

-  writing an ORM like **Django models** or **SQLAlchemy**
-  hijacking internal Python logic (e.g. like **pytest** does)
-  emulating JavaScript-like objects (the Prototype pattern)

Throughout 20 years of Python programming, I have not come across a
single situation where writing a metaclass was necessary. But it helps
to understand Python on a deeper level.

Simple Example
--------------

Execute the example in :download:`metaclasses.py` and see what it does.

Complex Example
---------------

Here is a complex example for illustrative purposes.
The code might drive you nuts, so consider yourself warned!

1. run the code
2. admire what is happening
3. try to understand what is happening
4. return to 1

Here is the code:

.. code:: python3

   class CrazyMonkeyPack(type):

       def __new__(mcs, name, bases, dict):
           cls = type.__new__(mcs, name, bases, dict)

           def wrapper(*args):
               instance = []
               for i in range(1, args[0]+1):
                   monkey = cls(f'monkey #{i}')  # calls __init__
                   monkey.state = 'crazy'  # monkey-patches the state attribute
                   instance.append(monkey)
               return instance

           return wrapper


   class CrazyMonkeys(metaclass=CrazyMonkeyPack):
       """A self-expanding horde of monkeys"""
       def __init__(self, name):
           self.name = name

       def __repr__(self):
           return f"<{self.name} ({self.state})>"


   monkeys = CrazyMonkeys(3)  # calls __new__
   print(monkeys)             # see what happens!


.. warning::

   Don't try using metaclasses at work, unless

   -  you have excluded all alternatives
   -  you really know what you are doing
   -  you have talked to an experienced developer
