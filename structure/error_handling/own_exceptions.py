"""
Example: Creating your own exceptions

Exercise: Construct a try.. catch clause that
prevents the Exception from being shown.

"""

class NoNumberError(Exception): pass


VALID_INPUT = ["1", "2", "3", "4"]


def get_text():
    text = input("please enter a number between 1-4: ")
    if not text in VALID_INPUT:
        raise NoNumberError("{} is not a number between 1-4.".format(text))
    return text


get_text()

                            
