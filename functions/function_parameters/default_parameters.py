"""
Examples of named parameters
"""
def addition(a=2, b=2, c=2):
    return a + b + c


print(addition(3, 3, 3))
print(addition(3, 3))
print(addition(3))
print(addition())
print(addition(b=4))
print(addition(b=4, c=5))

# partial assignment of parameters
from functools import partial

x = partial(addition, c=7, a=2)
print(x(b=5))