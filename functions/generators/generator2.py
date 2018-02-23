"""
Generator with an endless loop.
"""
def count():
    n = 1
    while True:
        yield n
        n *= 2


gen = count()

print(next(gen))
print(next(gen))
print(next(gen))
