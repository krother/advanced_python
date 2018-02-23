
import time


def timestamp(func):
    def wrapper(*args):
        result = func(*args)
        print(time.asctime(),'   ', str(result))
        return result

    return wrapper


@timestamp
def slow_addition(a, b):
    time.sleep(0.5)
    return a + b

@timestamp
def slow_multiplication(a, b):
    time.sleep(1)
    return a * b


slow_addition(1, 1)
slow_addition(3, 4)
slow_multiplication(3, 4)
slow_addition(10, 10)
slow_multiplication(10, 10)
