# Decorators

In general, **decorators are functions that manipulate functions**.
More specifically, a decorator wraps a function to add extra behavior to a function call.

In the examples below, we will decorate a Python function that calculates fibonacci numbers.


## Using built-in decorators

Most of the time, you will use built-in decorators.
One example is `functools.lru_cache` that memorizes the output of a function to save time later.
Let's decorate a function with it:

    :::python
    from functools import lru_cache

    @lru_cache
    def fibonacci(n):
        """Recursively calculates fibonacci numbers"""
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)
    
Try calculating a recursive fibonacci number for `n=50` without the decorator.
It takes forever!
By default, `lru_cache` memorizes the last 128 results, so above that the recursive fibonacci becomes slow again.

Built-in decorators are also used in:

* web frameworks like **Flask** to assign URLs to Python functions
* the **pytest** framework to create compact test code
* classes with `@property` and `@staticmethod` (described in the OOP section)

----

## Writing your own decorators

If want to add functionality for which no decorator exists, e.g. printing a timestamp for every addition, you could define a new function:

    :::python
    import time

    def fibonacci_with_timestamp(n):
        print(time.asctime())
        return fibonacci(n)

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
    def fibonacci(n):
        """Recursively calculates fibonacci numbers"""
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)


You can argue that this does not simplify the code in the first place.
Using decorators pays off in bigger programs, when they are used often,
or imported from different modules.

Most of the time, you would use predefined decorators. Notable places are

----

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
    def fibonacci(n):
        """Recursively calculates fibonacci numbers"""
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)


    # check docstring - would not work without @wraps
    print(help(addition))
