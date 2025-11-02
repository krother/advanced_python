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
