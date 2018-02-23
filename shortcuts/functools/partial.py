
from functools import partial

def add(a, b):
	return a + b


add3 = partial(add, 3)
print(add3(5))

