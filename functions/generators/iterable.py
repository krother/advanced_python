"""
Use iter() to create a generator from an iterable.
"""
words = [(455, 'sea'),
         (336, 'boat'),
         (281, 'white'),
         (1226, 'whale'),
         (329, 'captain'),
         (510, 'Ahab')
          ]


def add_bars(data):
    """Prints a horizontal bar every two lines."""
    g = iter(data)
    while 1:
        yield next(g)
        yield next(g)
        print('-' * 16)
        

for x in add_bars(words):
    print("%-10s:%5i" % (x[1], x[0]))

