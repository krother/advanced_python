"""
Comprehensions
"""

from random import randint
from pprint import pprint

# List comprehensions
numbers = [randint(1, 50) for i in range(50)]
print(numbers, end='\n\n')


by_seven = [x for x in numbers if not x % 7]
print(by_seven)

