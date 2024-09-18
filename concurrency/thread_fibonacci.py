"""
Fibonacci with threads
# adopted from
http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/
"""

import threading
import time
import random


class FibonacciThread(threading.Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    @staticmethod
    def fibo(n):
        if n == 0:
            return 1
        else:
            return n * FibonacciThread.fibo(n - 1)

    def run(self):
        result = self.fibo(self.number)
        time.sleep(random.randint(5, 20))
        print(f"{self.number}! = {result}")


for number in range(10):
    FibonacciThread(number).start()
