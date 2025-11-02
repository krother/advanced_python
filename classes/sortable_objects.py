from pprint import pprint

class Elephant:
    """Elephants that sort themselves by trunk size"""
    def __init__(self, name, trunk_size):
        self.name = name
        self.trunk_size = trunk_size

    def __repr__(self):
        return f"<{self.name} [trunk {self.trunk_size}]>"

    def __lt__(self, other):
        return self.trunk_size < other.trunk_size

elephants = [
    Elephant('mama', 5),
    Elephant('baby', 1),
    Elephant('grandma', 7),
    Elephant('daddy', 6),
    Elephant('son', 3),
]


pprint(elephants)

print("\nAnd now the biggest elephants go first:")
elephants.sort()

pprint(elephants)
