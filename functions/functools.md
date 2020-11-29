
# Map-Filter-Reduce

Python offers many functions that can be used to implement patterns from *functional programming*.

**Functional Programming** is a programming philosophy where a program is defined by functions. These functions are stateless (i.e. there are no global variables).
This paradigm helps designing distributed and concurrent algorithms.

Although one would rarely implement these in pure Python, it is a good exercise.
Functional code often comes out very clean and is easy to debug and maintain.

A side effect is that it helps you to avoid class-based implementations, which often are more wordy.

## Map

The `map()` function applies a function to all elements of an iterable.
It is returning a generator. `map()` is an alternative to a comprehension.

    :::python
    def square(x):
        return x ** 2

    squares = map(square, numbers)
    print(squares)
    print(list(squares))


## Filter

The  `filter()` function returns all elements of an iterable for which a function returns `True`.
It is the functional equivalent of the `if` clause in a comprehension.

    :::python
    def odd(x):
        return x % 2 != 0

    odd_numbers = filter(odd, range(10))
    print(odd_numbers)
    print(list(odd_numbers))


## Reduce

    :::python
    from functools import reduce

    numbers = [1, 2, 3, 4, 5, 6, 7, 8]


    # reduce
    def add(x, y):
        return x + y

    print(reduce(add, numbers))
    print(reduce(add, [[1, 2, 3], [4, 5, 6]]))

    from functools import partial

    def add(a, b):
    	return a + b


    add3 = partial(add, 3)
    print(add3(5))


    from functools import reduce

    words = [
        (455, 'sea'),
        (336, 'boat'),
        (281, 'white'),
        (1226, 'whale'),
        (329, 'captain'),
        (510, 'Ahab')
    ]


    def newlines(a, b):
        return a + '\n' + b


    def wordformat(x):
        return "{:>10s}:{:5d}".format(x[1], x[0])


    print(reduce(newlines, map(wordformat, words)))

## Partial

The ``functools`` module contains a couple of ways to manipulate
functions.

The ``partial`` fills in a part of the parameters, resulting in a new
function:

    :::python
    add5 = functools.partial(addition, 5)
    print(add5(8))  # results in 13


## Caching

The ``lru_cache`` decorator caches results, so that the second call with
the same parameters is faster. It is useful when your function is fully
deterministic.

    :::python
    from functools import lru_cache

    @lru_cache()
    def fibonacci(n):
        if n < 2:
            return n
        return fibonacci(n-1) + fibonacci(n-2)

    print(fibonacci(50))

Try the program with and without the decorator!
