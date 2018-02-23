"""
Exercise:

Examine the performance of the loop.

T
"""
from random import randint

numbers = [randint(1, 1000) for i in range(100000)]


squares = []
for x in numbers:
	squares.append(x ** 2)
