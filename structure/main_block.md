
# Structure of a Python script

There is a standard structure recommended for Python scripts:

1. imports
2. constants
3. functions and classes
4. `__main__` block

## Example

The following program contains most of these elements

    :::python
    from pprint import pprint

    MESSAGE = "Good morning {}. Nice to see you!"

    def hello(name):
        """Writes a hello world message"""
        msg = MESSAGE.format(name)
        pprint(msg)

    if __name__ == '__main__':
        name = input("please enter your name: ")
        hello(name)

## Imports

All import statements should be grouped together at the beginning of a Python file.
If you have lots of imports, a standard for sorting them might be useful. The tools **isort** and **black** help with that.

## Constants

In Python, constants do not exist as a syntax element.
But it is a good practice to group variables *"that the programmer does not intend this variable to change".

These constants should be written in capitals to distinguish them from variables that change during their lifetime.

## Function and Class definitions

Functions and classes should be defined in nested-first-order. That means functions called by other functions go first, functions called from the main program only go last.

## The __main__ block

At the end of the program, there is a strange construct:
The `if __name__ == '__main__':` block indicates the main program.

The `__main__` block is only executed when you run the entire program with `python my_program.py` (or the equivalent in your editor). However, it is **not** executed when you import functions or classes from it. This way you can have a main program and reusable functions in the same file.

It you can keep an entire code block here, or only call a `main()` function. Sometimes the `__main__` block is used for other things (e.g. test code).
