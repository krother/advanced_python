Classes
=======

What are classes?
-----------------

.. figure:: classes.png

Classes are a tool to manage complexity in a program. They group two
things in a single structural unit: **attributes (data)** and **methods
(behavior)**.

In more simple terms, you can use a class to stuff complexity into it,
so that your main program becomes simple. In my opinion, this way of
structuring code should be the main motivation to using classes in
Python.

In this chapter, you find an example how to use a class to structure your code.

--------------

Defining a class
----------------

To define a class, you need to define three things:

-  give the class a name in ``CamelCase``)
-  define attributes (variables that belong to the class)
-  define methods (functions that belong to the class)

In the code below, a class for a **Planet** is defined:

.. literalinclude:: planet.py

The class ``Planet`` contains three attributes
and two methods.

Note that you need to add the word ``self`` every time you refer to an
attribute. You also must use ``self`` as the first parameter in every
method of a class.

Creating Objects
----------------

To use a class, you need to create an object from it first. Objects are
*“live versions”* of a class, the class being an idealized abstraction
(in the sense of `Platos Theory of Forms <https://en.wikipedia.org/wiki/Theory_of_forms>`__).
If you think of **Planet** as a class, the actual planets **Earth** and **Pandalor**
would be the objects of that class.

You can create multiple objects from a class, and each object has its
own, independent attributes. Syntactically, you can think of a class as a function that returns
objects. (This is a gross oversimplification to what textbooks on
classes say, but in Python it is more or less what happens).

To create ``Planet`` objects, you need to call the class. Creating an
object will automatically call the constructor ``__init__(self)`` with
the parameters supplied.

.. code:: python3

   earth = Planet(name="Earth", description="the blue planet")
   pandalor = Planet(name="Pandalor", description="home of the space pandas")
   arcturus = Planet(name="Arcturus", description="an icy planet, home of penguins")


Then you can access the attributes like any variable using the dot (``.``) syntax:

.. code:: python3

   print(earth.name)
   print(earth.balance)

Exercise: Methods
-----------------

And you can call methods in a similar way:

.. code:: python3

   earth.add_connection(pandalor)
   earth.add_connection(arcturus)

   earth.show_connections()

Note that these methods modify the state of the planet *Earth*, but not the other two.

Implement the `show_connections()` method using the code from the program `space_game.py`.

Exercise: Refactor using classes
--------------------------------

Simplify `space_game.py` using the `Planet` class.


Four Ways to create classes
---------------------------

Python knows multiple flavors of defining and using classes.
These are recent developments (~2018+), strongly relying on the availability of **Type Hints**.

Execute and examine the following code examples, defining a level for a point-eating game:

- :download:`class_vanilla.py`
- :download:`class_typedict.py`
- :download:`class_dataclass.py`
- :download:`class_pydantic.py`

--------------

Caveats
-------

In other programming languages classes are often advertised for
*“modeling real-world objects or logical entities”*. This is partially
true in Python. Note that Python offers a lot of alternatives to using
classes, e.g. dictionaries, named tuples or DataFrames may often serve
the same purpose equally well.

Another motivation for using classes you find in textbooks is
**encapsulation**, isolating parts of your program from the rest.
Encapsulation does not exist in Python (e.g. you cannot declare parts of
a class as ``private`` in a way that cannot be circumvented). If you
depend on your code being strictly isolated from other parts (e.g. in a
security-critical application or when organizing a very large program),
**consider other programming languages than Python.**

--------------

.. topic:: Dirty Tricks

   Python allows using classes in multiple creative ways.
   I call them **dirty tricks**. Most of them have their uses in
   larger programming libraries. But if you are writing a smaller program,
   they probably do more harm than good.

   Especially if you are still learning about classes, consider yourself
   warned of the following tricks:
   
   -  Multiple Inheritance
   -  Operator Overloading
   -  Metaclasses
   -  Monkey Patching
   
   These dirty tricks are likely to mess up your program. Do not use any of
   them unless you really know what you are doing!
