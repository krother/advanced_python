
from timeit import timeit
from random import random

N = 100000

def front_to_end(data):
    elem = data.pop(0)
    data.append(elem)


class ChainElement:

    def __init__(self, val):
        self.value = val
        self.next = None


class ChainedList:

    def __init__(self, n):
        self.first = ChainElement(random())
        self.last = self.first

        for i in range(n-1):
            self.last.next = ChainElement(random())
            self.last = self.last.next

    def front_to_end(self):
        self.last.next = self.first
        new_first = self.first.next
        self.last = self.first
        self.first.next = None
        self.first = new_first


data = [random() for i in range(N)]
chain = ChainedList(N)

t1 = timeit('front_to_end(data)', globals=locals())
t2 = timeit('chain.front_to_end()', globals=locals())

print(f"time --- list: {t1:6.3}   chained: {t2:6.3}")
