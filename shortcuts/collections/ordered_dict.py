"""
OrderedDict: a dictionary that preserves insertion order

Remark: the newest Python versions will have this as default behavior
"""

from collections import OrderedDict
from pprint import pprint


names = [
         "Adam", "Bea", "Charlie", "Danielle",
         "Eve", "Frantz", "Gustav", "Helena"
        ]

od = OrderedDict()

for i, name in enumerate(names):
    od[i] = name

pprint(od)

od.move_to_end(2)
pprint(od)
