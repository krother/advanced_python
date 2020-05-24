"""
Organizing data with named tuples
"""

from collections import namedtuple


Animal = namedtuple('Animal', ('name', 'legs', 'eggs', 'extinct'))


species = [
    Animal('Chicken', 2, True, False),
    Animal('Caenorhabditis', 0, 'no idea', False),
    Animal('Platypus', 4, True, False),
    Animal('Chimp', 2, False, False),
    Animal('T-Rex', 2, True, True),
    Animal('Dolphin', 0, False, False),
]


print('Animals with 2 legs:')
for animal in species:
    if animal.legs == 2:
        eggs = "lays eggs" if animal.eggs else "gives live birth"
        extinct = " and is extinct." if animal.extinct else ""
        print("{:>20s} {}{}.".format(animal.name, eggs, extinct))
