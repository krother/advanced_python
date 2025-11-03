
import time


def ticker(delta:float):
    """yields True if 'delta' seconds passed since the last tick."""
    last = time.time()  # processor time in seconds
    while True:
        current = time.time()
        if current - last >= delta:
            last = current
            yield True
        else:
            yield False


t = ticker(delta=2.0)
v = ticker(delta=5.0)

i = 10
while i > 0:
    if next(t):
        print("tick")
        i -= 1
    if next(v):
        print("tack")

