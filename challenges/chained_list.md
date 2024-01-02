
# Chained List

**🎯 Identify strengths and weaknesses of data structures.**

## Cycle Entries

In this problem, we need to **remove the first element of a sequence** and **add it to the end**.

An implementation using a Python list could look like this:

    :::python3
    from random import random

    def front_to_end(data):
        elem = data.pop(0)
        data.append(elem)

    N = 100
    data = [random() for i in range(N)]
    front_to_end(data)

----

## Measure time behavior

This operation looks harmless. Is it?

Use the `timeit` module to find out how long it runs.
The following code sniplet prints out the time needed:

    :::python3
    from timeit import timeit

    t = timeit('front_to_end(data)', globals=locals())
    print(f"time used: {t:6.3}")

Now scale up N (by adding one or more zeros) and see how the time changes.

----

## Using a Chained List

Let's try an alternative data struture: the **chained list**.
In a chained list, each element points to the next element in the chain (or `None` if it is the last element in the chain).

It is common to keep the first and last element of a chain in extra variables.
Here is a Python implementation using classes:

    :::python3
    class ChainElement:

        def __init__(self, val):
            self.value = val
            self.next = None


    class ChainedList:
        """Helper class to manage the elements of a chain"""

        def __init__(self, n):
            self.first = ChainElement(random())
            self.last = self.first

            for i in range(n-1):
                self.last.next = ChainElement(random())
                self.last = self.last.next

        def front_to_end(self):
            """move the first element of the chain to the end"""
            ...

    # create a chained list
    chain = ChainedList(N)
    chain.front_to_end()

----

## The Challenge

* implement the `front_to_end()` method so that it does an operation equivalent to the list function above
* measure the time required for `front_to_end()` (without creating the chain)
* try different values of N and compare the result to the list-based implementation
* what are the pros and cons of either implementation?
