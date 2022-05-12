
# Decorators with a Metaclass

**🎯 Implement the decorator `add_two`, so that the following code:**

    @add_two
    def double(a):
        return a * 2

    print(double(20))
    print(add_two(40))

**results in:**

    42
    42

Do not modify the above code!

## Hints

In this task you can practice the following concepts:

* Decorator functions
* Decorator Classes
* Metaclasses

A **decorator class** and a **function** are different things, aren't they?
In Python this is not necessarily the case! Any Python object can behave like any other.

Fans of strongly typed languages will cringe during this exercise. However, implementing a decorator that behaves like a function is a good way to understand the deeper machinery of namespaces and dynamic typing in Python.


## Optional Goal 1

If the exercise was too easy for you, implement the decorator as a class. For this you have to deal with the term `metaclass`.

## Optional Goal 2

The decorator should still work if it is stacked several times on top of each other:

    @add_two
    @add_two
    def double(a):
        return a * 2

    double(19)

shall result in `42`.

*Translated with [www.DeepL.com](www.DeepL.com/Translator)*
