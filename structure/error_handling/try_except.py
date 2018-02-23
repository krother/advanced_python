"""
Example: catching_exceptions
"""

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# print all cards with numbers divisible by 2:
for card in cards:
    try:
        number = int(card)
        if number % 2 == 0:
            print(card, "is an even card.")
    except ValueError:
        print(card, "can not be divided")
    else:
        print(card, "could be divided")
    finally:
        print("next number.")

