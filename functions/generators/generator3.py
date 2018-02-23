"""
Generator with a finite loop
can be used with for
"""
def count():
    n = 1
    while n < 1000:
        yield n
        n *= 2


gen = count()

for number in gen:
    print(number)
