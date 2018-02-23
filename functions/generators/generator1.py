"""
Minimalistic generator function.
"""
def count():
    yield 1
    yield 2
    yield 4
    yield 8
    yield 16
    yield 32
    yield 64
    yield 128
    yield 256


gen = count()

print(next(gen))
print(next(gen))
print(next(gen))
