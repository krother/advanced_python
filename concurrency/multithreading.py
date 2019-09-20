
# adopted from http://www.devshed.com/c/a/Python/Basic-Threading-in-Python/1/

import threading
import time
import random


number = 1

class MyThread (threading.Thread):

    def run(self):
        global number
        print('This is thread ' + str(number) + ' speaking.')
        n = number
        number += 1
        for i in range(20):
            print('Thread', n, 'counts', i)
            time.sleep(1 * random.randint(1, 10))


for x in range(10):
       MyThread().start()
