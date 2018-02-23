"""
Map, filter and reduce
"""

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8]


# map
def square(x):
    return x ** 2

squares = map(square, numbers)
print(squares)
print(list(squares))


# filter
def by_four(x):
    return x % 4 == 0

by_four = filter(by_four, map(square, numbers))
print(by_four)
print(list(by_four))


# reduce
def add(x, y):
    return x + y

print(reduce(add, numbers))
print(reduce(add, [[1, 2, 3], [4, 5, 6]]))
