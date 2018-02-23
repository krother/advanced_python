
from functools import reduce

words = [
    (455, 'sea'),
    (336, 'boat'),
    (281, 'white'),
    (1226, 'whale'),
    (329, 'captain'),
    (510, 'Ahab')
]


def newlines(a, b):
    return a + '\n' + b


def wordformat(x):
    return "{:>10s}:{:5d}".format(x[1], x[0])


print(reduce(newlines, map(wordformat, words)))
