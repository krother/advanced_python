"""
defaultdict: a dictionary with a function that supplies default values.
"""

from collections import defaultdict
from random import choice, randint
from pprint import pprint


names = [
         "Adam", "Bea", "Charlie", "Danielle",
         "Eve", "Frantz", "Gustav", "Helena"
        ]


# dict initialized with zero
dd = defaultdict(int)

for i in range(100):
    key = choice(names)
    dd[key] += 1

pprint(dd)


# dict initialized with empty list
dd = defaultdict(list)

for key in names:
    for i in range(3):
        dd[key].append(randint(1, 10))

pprint(dd)
