"""
Example of parallel execution with asyncio

see:
https://docs.python.org/3/library/asyncio-task.html
"""
import asyncio
import random
from functools import reduce


def multiply(a, b):
    return a * b


async def factorial(number):
    """delayed calculation of fibonacci number"""
    result = reduce(multiply, range(1, number + 1), 1)
    delay = random.randint(5, 20)
    await asyncio.sleep(delay)
    print(f"after {delay:2} seconds: {number}! = {result}")


async def main():
    # create concurrent tasks
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(factorial(i)))

    # wait for tasks to finish
    # (all have to be awaited)
    for t in tasks:
        await t


# run the toplevel async function
asyncio.run(main())
