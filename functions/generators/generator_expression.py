"""
Generator expressions: list comprehensions without lists

Exercise: Add 9's to the range until the program becomes slower.
"""

squares = (x ** 2 for x in range(99))

print(squares)
print(next(squares))
print(next(squares))
print(next(squares))
