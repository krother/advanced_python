Abstract Base Classes
=====================

If you want to use inheritance but not allow instances of the
superclass, you can use the **ABC Metaclass**. With ``ABCMeta``, you
need to create a subclass that overwrites all abstract methods and
properties:

.. code:: python3

   from abc import ABCMeta, abstractmethod, abstractproperty

   class AbstractAnimal(metaclass=ABCMeta):

       @abstractmethod
       def make_noise(self):
           pass

       # an abstract read-only-property
       @abstractproperty
       def species(self):
           pass

       # abstract read/write property
       def getname(self):
           pass

       def setname(self, value):
           pass

       name = abstractproperty(getname, setname)

       # non-abstract method
       def is_alive(self):
           return True


Exercise 1: Abstract Animals
----------------------------

Implement the Dog class so that the code below runs.

.. code:: python3

   class Dog(AbstractAnimal):

       ...

   rex = Dog()
   rex.name = 'Rex'
   print(rex.is_alive())
   rex.make_noise()
   print(rex.species())

Exercise 2: Descriptors
------------------------

The example in :download:`descriptors.py` uses the **descriptor protocol**, a mechanism to control the getting and setting of attributes using object composition. 

Create both valid and invalid instances of the defined class.


Exercise 3: Game Objects
------------------------

Create a superclass `GameObject` for the classes in your game.
Use the following example code:

.. code:: python3

    from abc import ABC, abstractmethod

    class Command(ABC):
    
        def __init__(self, name):
            self.name = name

        @abstractmethod
        def executed(self):
            pass

