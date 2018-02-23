"""
Caching

Measure the time that calls of fibonacci() take to complete.

Then add the decorator functools.lru_cache to the function.
Measure the time again.

See: https://docs.python.org/3.6/library/functools.html
"""

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(30))
