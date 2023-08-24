
# Binary Search

**🎯 Measure the performance of an algorithm.**

## A search problem

Suppose you have a list of 1 million numbers:

    :::python3
    from random import randint, seed

    seed(42)
    N = 1_000_000
    ids = [randint(1_000_000, 9_000_000) for i in range(N)]

We want to know at which position the number `8997173` occurs – or whether it occurs at all.

----

## Brute-force solution

Of course, you could loop through all the numbers:

    :::python3
    def search(query, ids):
        """brute-force search"""
        for i in ids:
            if i == query:
                return i
        return -1

    search(8997173, ids)

Because of the `for` loop, the time cost of this function grows **linearly**.
If you search twice as much data, it will take twice as long.
The **Big-O-Notation** for this would be O(N).

----

## Recursive solution

An alternative approach is **binary search**, one of the most fundamental recursive algorithms:

    :::python3
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
    binary_search(8997173, ids, 0, len(ids))

The function requires the data to be sorted.
The search itself runs in **O(log N)** or **logarithmic** time.
If you search twice as much data, only one extra recursion is necessary.

### Visual Explanation

![BINÄRY SEARCH](../images/binary-search.png)

*source: idea-instructions.com, CC-BY-NC-SA 4.0*

----

## Challenge

Measure the time it takes both algorithms to run on 1 million numbers.
In IPython/Jupyter, you can use the magic function `%time`:

    :::python3
    In [2]: %time search(8997173, ids)

Compare the time required by the brute-force and binary implementations.
Then increase the size of the data by factor 10 and repeat the measurement.

### Questions

* Which of the searches is faster?
* How much time does the sorting take?
* When does binary search pay off?
* For what data would the brute-force algorithm be faster?
