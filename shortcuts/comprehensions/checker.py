"""
Explain the code
"""

def square(x, y):
    return "#" if (x+y) % 2 == 0 else "_"

checker = '\n'.join([''.join([square(x, y) for x in range(8)]) for y in range(8)])
print(checker)
