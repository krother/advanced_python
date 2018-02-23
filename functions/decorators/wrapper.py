"""
Wrapping a decorator, so that the decorated function
looks like the original one.

Exercise: Decorate the 'wrapper' function with:

    @wraps(func) 

Then run the program again.
"""
import time
from functools import wraps


def timestamp(func):

    def wrapper(*args):
        result = func(*args)
        print(time.asctime(),'   ', str(result))
        return result

    return wrapper


@timestamp
def fast_addition(a, b):
    """This function adds two arguments a,b and returns the result"""
    return a + b


fast_addition(1, 1)
fast_addition(3, 4)

print("name of the function:", fast_addition.__name__)
print("documentation string:", fast_addition.__doc__)
