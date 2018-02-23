"""
Example: local variable scope

Guess the value of the variable 'a' at the end of the program?

1) In the code as it is?
2) With the statement 'global a' inserted before the line 'a = number1 + number2'
3) With the statement 'global a' inserted after the line 'a = number1 + number2'

Verify your expectations
"""

def addition(number1, number2):
    """Just adds two numbers."""
    a = number1 + number2
    return a


a = 3
b = 5
c = addition(a, b)
