"""
Counter: A shortcut for a dictionary that counts
"""

from collections import Counter
from random import choice
from pprint import pprint


names = [
         "Adam", "Bea", "Charlie", "Danielle",
         "Eve", "Frantz", "Gustav", "Helena"
        ]

# generate 100 random names
data = [choice(names) for i in range(100)]

c = Counter(data)

pprint(c)
print(c['Adam'])
pprint(c.most_common(3))
