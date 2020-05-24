
# Named Tuples

The `namedtuple` type is a shortcut for structuring data.
A `namedtuple` has fixed fields.
If you are thinking about creating a class only for organizing attributes, the `namedtuple` is much shorter.

You define a `namedtuple` by listing its attributes:

    :::python
    from collections import namedtuple

    Animal = namedtuple('Animal', ('name', 'legs', 'eggs'))

    species = [
        Animal('chicken', 2, True),
        Animal('dolphin', 0, False),
        Animal('elephant', 4, False),
    ]

The attributes are available afterwards by their name.
This is much easier than indexing by numbers like in a normal tuple:

    :::python
    for animal in species:
        print(f"The {animal.name} has {animal.legs} legs.")
        if animal.eggs:
          print("It is laying eggs.")
