# Abstract Base Classes

If you want to use inheritance but not allow instances of the superclass, you can use the **ABC Metaclass**.
With `ABCMeta`, you need to create a subclass that overwrites all abstract methods and properties:

    :::python3
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

----

## Exercise

Implement the Dog class so that the code below runs.

    :::python3
    class Dog(AbstractAnimal):

        ...

    rex = Dog()
    rex.name = 'Rex'
    print(rex.is_alive())
    rex.make_noise()
    print(rex.species())
