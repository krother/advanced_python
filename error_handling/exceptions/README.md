
# Handling Exceptions

### Raising Exceptions

You can create errors with your own messages that stop the program:

    :::python
    raise ValueError("expected a valid Pokemon name")

## Catching Exceptions

The `try.. except` clause allows your program to catch errors and act on them
instead of terminating the program.

    :::python
    cards = "234567890JQKA"

    for card in cards:
        try:
            number = int(card)
            print(f"dealt {card}")
        except ValueError:
            print(f"{card} could not be dealt")

### How not to catch Exceptions

Exceptions should always be caught with an explicit error type.
Using a generic `except` makes debugging difficult:

    :::python
    cards = "234567890JQKA"

    for card in cards:
        try:
            number = int(card)
            print(f"dealt {car}")
        except:
            print(f"{card} could not be dealt")

In this example, `car` causes a `NameError` for every card. You don't get any clues what exactly went wrong.

This is called the *"diaper pattern"* and considered a very bad habit.

### Creating your own Exceptions

You can define your own types of Exceptions:

    :::python
    class WrongInputError(Exception): pass

and raise them:

    :::python
    text = input("please enter a number between 1-4: ")
    if not text in "1234":
        raise WrongInputError("{} is not a number between 1-4.".format(text))

The `try..except` works for your own Exception types as well.
