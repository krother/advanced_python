
# create random numbers
from random import randint, seed

seed(42)
N = 1_000_000
ids = [randint(1_000_000, 9_000_000) for i in range(N)]


def search(query, ids):
    """brute-force search"""
    for i in ids:
        if i == query:
            return i
    return -1

def binary_search(query, ids, start, stop):
    """recursive binary search"""
    if ids[start] == query:
        return start
    elif stop - start <= 1:
        return -1
    split = start + (stop - start) // 2
    if ids[split] > query:
        return binary_search(query, ids, start, split)
    else:
        return binary_search(query, ids, split, stop)

ids.sort()

#%timeit search(8997173, ids)

#%timeit binary_search(8997173, ids, 0, len(ids))
