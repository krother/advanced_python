
# Operator Overloading

In Python, classes can have **many** `__magic_methods__()` – those that start and end with a double underscore.
All `__magic_methods__()` have a special function and should never be called directly.
Most of them directly map to Python operators. Here are some examples:

| method | description |
|--------|-------------|
| `__init__()` | called when creating an object from a class |
| `__repr__()` | called when converting object to a string |
| `__add__()` | called when using the `+` operator on an object |
| `__mul__()` | called when using the `*` operator on an object |
| `__gt__()` | called when comparing the object to another |
| `__len__()` | called when using `len()` |
| `__hash__()` | called when using the object as a dictionary key |

It is often questionable, whether overloading operators is a good idea.
Many times it is not, because it obscures what is happening behind the scenes.

Compare the clarity of:

    :::python3
    a = vec1 * vec2
    b = vec1 @ vec2

versus

    :::python3
    a = vec1.dot_product(vec2)
    b = vec1.scalar_product(vec2)

Below you find two examples that I have found useful:

----

## Sortable Objects

The method `__gt__(self, other)` is implicitly called when comparing two objects, as done by any sorting algorithm.

    :::python3
    class Elephant:
        """Elephants that sort themselves by trunk size"""
        def __init__(self, name, trunk_size):
            self.name = name
            self.trunk_size = trunk_size

        def __repr__(self):
            return f"<{self.name} [trunk {self.trunk_size}]>"

        def __gt__(self, other):
            return self.trunk_size < other.trunk_size

    elephants = [
        Elephant('mama', 5),
        Elephant('baby', 1),
        Elephant('grandma', 7),
        Elephant('daddy', 6),
        Elephant('son', 3),
    ]

    from pprint import pprint

    pprint(elephants)

    print("\nAnd now the biggest elephants go first:")
    elephants.sort()

    pprint(elephants)


----

## Hashable Vectors

This is a 2D vector class I used for screen positions in a game.
I wanted the vectors to be capable of simple arithmetics.
They also needed to be hashable (which NumPy arrays are not).

    :::python3
    class Vector:

        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __add__(self, other):
            x = self.x + other.x
            y = self.y + other.y
            return Vector(x, y)

        def __sub__(self, other):
            x = self.x - other.x
            y = self.y - other.y
            return Vector(x, y)

        def __mul__(self, n):
            '''scalar multiplication'''
            # considered unclean - for illustration only
            x = self.x * n
            y = self.y * n
            return Vector(x, y)

        def __hash__(self):
            return str(self).__hash__()

        def __repr__(self):
            return f'[{self.x};{self.y}]'


    UP = Vector(0, -1)
    LEFT = Vector(-1, 0)
    UPLEFT = UP + LEFT
    FAST_UP = UP * 3

    messages = {
      UP: 'moving up',
      LEFT: 'moving left',
    }
