"""
Dict Comprehensions
"""

from random import randint
from pprint import pprint


squares = {x: x**2 for x in range(16)}
pprint(squares)

print('\n', '-' * 40, '\n')

asc = {char: ord(char) for char in "Hello World"}
pprint(asc)
