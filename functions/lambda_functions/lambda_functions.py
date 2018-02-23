
from random import randint

numbers = [randint(1,10) for x in range(12)]

odd = lambda x:x%2
even = lambda x:not odd(x)

print([x for x in numbers if odd(x)])
print([x for x in numbers if even(x)])
