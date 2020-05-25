# Decorators

In general, **decorators are functions that manipulate functions**. More
specifically, a decorator wraps a function to manage a function call.

Imagine you have the a Python function::

    :::python
    def addition(a, b):
        """add two arguments a,b and returns the result"""
        return a + b

If you now want to add functionality, e.g. printing a timestamp for every addition, you could define a new function:

    :::python
    import time

    def addition_with_timestamp(a, b):
        print(time.asctime())
        return addition(a, b)

If you want to **add the timestamp feature to many functions**, consider using a decorator:

    :::python
    def print_timestamp(func):
        def wrapper(*args):
            print(time.asctime())  # done before addition
            result = func(*args)   # calls the addition function
            ...                    # actions after addition
            return result
    return wrapper

    @print_timestamp
    def addition(a, b):
        """add two arguments a,b and returns the result"""
        return a + b


You can argue that this does not simplify the code in the first place.
Using decorators pays off in bigger programs, when they are used often,
or imported from different modules.

Most of the time, you would use predefined decorators. Notable places are

* the `functools` module
* classes with `@property` and `@staticmethod`
* the Flask web server
* pytest

## Wrapping Decorators

The **``wraps``** decorator copies documentation strings into the decorator function,
so that the decorated function looks like the original one.
It is useful when writing your own decorators.

    :::python
    import functools

    def print_timestamp(func):
        @functools.wraps(func)
        def wrapper(*args):
            print(time.asctime())  # done before addition
            result = func(*args)   # calls the addition function
            ...                    # actions after addition
            return result
    return wrapper

    @print_timestamp
    def addition(a, b):
        """add two arguments a,b and returns the result"""
        return a + b

    # check docstring - would not work without @wraps
    print(help(addition))
