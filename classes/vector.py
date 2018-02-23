"""
Examples of properties and operator overloading.
"""

class Vector:
    """
    Direction vectors for moves, positions etc.

    Vector objects can be used for simple arithmetics,
    like adding positions to each other.

    They are hashable, unlike NumPy arrays.
    """

    def __init__(self, *args):
        self.coord = tuple(args)

    @property
    def x(self):
        return self.coord[0]

    @x.setter
    def x(self, x):
        self.coord = (x, self.y)

    @property
    def y(self):
        return self.coord[1]

    @y.setter
    def y(self, y):
        self.coord = (self.x, y)

    def __add__(self, other):
        if not isinstance(other, Vector):
            other = Vector(other)
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        if isinstance(other, int):
            x = self.x * other
            y = self.y * other
        else:
            if not isinstance(other, Vector):
                other = Vector(other)
            x = self.x * other.x
            y = self.y * other.y
        return Vector(x, y)

    def __floordiv__(self, other):
        if isinstance(other, int):
            x = self.x // other
            y = self.y // other
        else:
            if not isinstance(other, Vector):
                other = Vector(other)
            x = self.x // other.x
            y = self.y // other.y
        return Vector(x, y)

    def __iter__(self):
        return self.coord.__iter__()

    def __eq__(self, other):
        if type(other) == type(self):
            if self.x == other.x and self.y == other.y:
                return True
        else:
            return Vector(self) == Vector(other)

    def __hash__(self):
        return str(self).__hash__()

    def __repr__(self):
        return '[%i;%i]' % (self.x, self.y)


ZERO_VECTOR = Vector(0, 0)
UP = Vector(0, -1)
DOWN = Vector(0, 1)
LEFT = Vector(-1, 0)
RIGHT = Vector(1, 0)
UPLEFT = Vector(-1, -1)
DOWNLEFT = Vector(-1, 1)
UPRIGHT = Vector(1, -1)
DOWNRIGHT = Vector(1, 1)
