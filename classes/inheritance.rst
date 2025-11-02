Inheritance
===========

Classes can extend other classes. A **subclass** will have all the
attributes and methods of a **superclass**. You can say the subclass
inherits from the superclass.

A subclass can define new methods and attributes. It can also replace
methods of the superclass.

The most important design principle when using inheritance is **Liskovs
Substitution Principle**. It says that you should be able to use a
subclass whereever the superclass is used.

--------------

Example
-------

Here you find an example using the ``Planet`` class defined earlier.

.. code:: python3

   class UnstablePlanet(Planet):
       """A planet that explodes after some time"""

       def __init__(self, name: str, description: str, countdown: int):
           super().__init__(name, description)
           self.countdown = countdown

       def ticker(self):
           if self.countdown > 0:
               self.countdown -= 1
           else:
               print(f"BOOOM! {self.name} exploded")


The ``super()`` function returns an instance of the superclass, so that
you can call the inherited methods, even if you are replacing them.

Using the subclass is very similar to using the superclass:

.. code:: python3

   cornflake = UnstablePlanet('Cornflake', 'a crumbling planet', countdown=10)
   while cornflake.coundown:
       cornflake.ticker()


Multiple Inheritance
--------------------

Python allows multiple inheritance, often found under the term **mixins**.
It is tricky, because the namespaces potentially collide.
I advise to avoid multiple inheritance whenever possible.

A lifesaver is checking the **method resolution order**, see :download:`multiple_inheritance.py`.


.. warning::

   **Caveat**

   Once you get the hang of object-oriented programming, inheritance is not
   that difficult. At some point, it is very tempting to define lots of
   subclasses, and class hierarchies with multiple levels. Most of the
   time, having one level of inheritance is enough. Many times you do not
   need inheritance at all, and you are better off using **object composition**.

