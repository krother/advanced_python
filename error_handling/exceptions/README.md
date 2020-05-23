
# Handling Exceptions

The `try.. except` clause catches errors and allows you to react on them.

    # print all cards with even numbers.
    cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    for card in cards:
        try:
            number = int(card)
            if number % 2 == 0:  # modulo operator
                print(card, "is an even card.")
        except ValueError:
            print (card, "can not be divided")

Normally, `int("J")` would terminate the program. The `except` clause allows the program to finish neatly.

In Python, Exceptions should always be handled explicitly. Using a generic `except` is considered a very bad habit, because it makes debugging difficult.


## Creating your own Exceptions

You can define your own types of Exceptions:

    class MyError(Exception): pass

and create an error using your own type:

    raise MyError("message")

and catch it:

    try:
        ..
        ..
    except MyError:
        ..