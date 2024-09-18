import sys
import time
import random

n = int(sys.argv[1])
result = 1

while n > 0:
    result *= n
    n -= 1

delay = random.randint(5, 15)
time.sleep(delay)
print(f"fibonacci of {sys.argv[1]} = {result} after {delay} sec")
