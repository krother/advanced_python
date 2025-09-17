
The Singleton Pattern
=====================

.. warning::

   In Python, real singletons do not exists. There are usually several ways to trick the interpreter to create multiple objects. However, we can make it very hard to create multiple objects *unintentionally*.

Change the `Repository` class from the previous chapter into a **Singleton**, of which there is only one instance.
Generally, there are two valid approaches:

- do not use a class in the first place, implement everything on the module level. Pythons **import library** (`importlib`) makes sure that every module gets loaded at most once.
- modify the metaclass. See the following code example:

.. code:: python3

    class Singleton(type):
        """metaclass that overrides Pythons standard object creation process"""
        def __init__(cls, name, bases, attrs, **kwargs):
            super().__init__(name, bases, attrs)
            cls._instance = None
    
        def __call__(cls, *args, **kwargs):
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
            return cls._instance
    
    
    class Repository(metaclass=Singleton):
        ...


.. seealso::

   the `Singleton Pattern <https://sourcemaking.com/design_patterns/singleton>`__

