
# Lambda Functions

The `lambda` expression allows you to define a function without the `def` statement:

    :::python
    names = ['Ada', 'Bob', 'Charlotte', 'Dave', 'Eddy']

    # find words with an odd/even number of characters
    odd = lambda s:len(s) % 2
    even = lambda s:not odd(s)

    print('odd :', [x for x in names if odd(x)])
    print('even:', [x for x in names if even(x)])

The advantage of `lambda` is that it can be combined with other functional expressions like `map()`, `filter()` and  `reduce()`:

    :::python
    odd_names = list(filter(lambda s:len(s) % 2, names))

Excessive use of `lambda` does not necessarily make your code more clean.
But if you would like to experiment with *functional programming* it is worth to know.
