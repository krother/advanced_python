
# Functions and Namespaces

## Exercise 1

Create two new Python files in your working directory:

    triangle.py

    a = 3
    b = 4

and

    rectangle.py

    a = 4
    b = 3


## Exercise 2

Import both modules from the command line or a third script and print the value of `a`. Consider the following variations:

    from triangle import a

    import triangle


## Exercise 3

Add the follow function to `triangle.py`:

    import math

    def calc_hypothenuse(a, b):
	    c = math.sqrt(a ** 2 + b ** 2)
	    return c

Import and call the function in your main module:

    c = calc_hypothenuse(4, 5)
    return c


## Exercise 4

Write a function `calc_area(a, b)` in `rectangle.py`.

## Exercise 5

Consider the following variations of the function definition:

    def calc_hypothenuse(a=3, b=4):
        ...
    
    def calc_hypothenuse(a, b=4):
        ...

    def calc_hypothenuse(a=3, b):
        ...

    ...
        return a, b, c

    def calc_hypothenuse():
        ...

## Exercise 6

Discuss the concepts of **variable scope** and **namespaces**
