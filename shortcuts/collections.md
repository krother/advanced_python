
# Collections

The `collections` module contains a few very useful dictionaries:

| type | description |
|------|-------------|
| Counter | dictionary for counting things |
| defaultdict | dictionary with a preset value |
| OrderedDict | dictionary preserving insertion order |

## Counter

The `Counter` is a special dictionary for counting things.

    :::python
    from collections import Counter

    # generate 100 random names
    names = ["Adam", "Bea", "Charlie", "Danielle",
             "Eve", "Frantz", "Gustav", "Helena"]
    from random import choice
    data = [choice(names) for i in range(100)]

You create a `Counter` by giving it an iterable:

    :::python
    c = Counter(data)

The most important new method is `most_common`. The rest works like a normal dictionary.

    :::python
    print(c)
    print(c.most_common(3))
    print(c.get('Adam'))


## Defaultdict

A `defaultdict` inserts a default value for each key that is used the first time.
It therefore never throws a `KeyError` when requesting a value.

### Creating a defaultdict

A `defaultdict` is created with a function that creates the default valued.

The following dictionary defaults to a zero integer:

    :::python
    from collections import defaultdict

    d = defaultdict(int)
    d['Adam'] = 33
    d['Eve'] = 55

    print(d['Adam'])  # -> 33 like a normal dict
    print(d['Guido']) # -> 0  because it's a new key

Most times a `defaultdict` is initialized with a data, but any Python function works. Try:

    :::python
    from random import random

    d = defaultdict(random)
    d['dummy']


### Collecting lists

A common use case is to create a dict of lists.
This becomes very easy with a `defaultdict`.

The following example sorts names by their initial:

    :::python
    names = [
            "Athene", "Ada", "Hypathia",
            "Anna", "Helena", "Thetis"
    ]

    d = defaultdict(list)

    for n in names:
        key = n[0]
        d[key].append(n)

This results in the following data:

    :::python
    defaultdict(list,
                {'A': ['Athene', 'Ada', 'Anna'],
                 'H': ['Hypathia', 'Helena'],
                 'T': ['Thetis']})


## OrderedDict

OrderedDict is a special kind of dictionary that preserves the insertion order.

    :::python
    from collections import OrderedDict

    od = OrderedDict()

    names = ["Adam", "Bea", "Charlie", "Danielle", "Eve", "Frantz", "Gustav", "Helena"]
    for i, name in enumerate(names):
         od[i] = name

With an OrderedDict, you have a guarantee that the output of the following command is always the same (which you don't have with a normal dictionary):

    :::python
    print(od)

You have an additional method for changing the order:

    :::python
    od.move_to_end(2)
    print(od)
