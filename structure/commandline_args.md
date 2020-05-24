# Command-line Arguments

One easy way to use your programs more flexibly is through calling them with command-line arguments from a terminal:

Two ways to implement CL arguments are **sys.argv** and **argparse**.

## Option 1: sys.argv

The `sys.argv` method is a quick-and-dirty approach.
It is quick to implement, but not very clean in the long run.

The list `sys.argv` contains everything that was entered on the terminal.
For instance, if you write

    :::bash
    python hello.py Kristian

the `sys.argv` list will contain two strings:

    :::python
    ['hello.py', 'Kristian']

You can access these values in your code like this:

    :::python
    import sys

    if len(sys.argv) == 2:
        name = sys.argv[1]
        print(f'Hello {name}')
    else:
        print("usage: hello.py <name>")

## Option 2: argparse

This is a cleaner version. `argparse` allows you to define command-line parameters for a Python application. The module takes care of reading the parameters into variables, checking data types and generating help text.

`argparse` is installed with Python by default.

### Usage

1. Define the `argparse` options in your code (in a function or your main block).
2. Call `args = parser.parse_args()`
3. Access your options as attributes of `args`

In addition to using your option, your program will print usage instructions when you type

    :::bash
    python myprog.py --help

### Example

Here is a hello world program that you can use as a starting point:


    import argparse

    parser = argparse.ArgumentParser(description='A Hello World program with arguments.')

    parser.add_argument('-m', '--message', type=str, default="Hello ",
                   help='message to be written')

    parser.add_argument('-c', '--capitals', type=bool,
                   help='write capitals')

    parser.add_argument('name', type=str, nargs='+',
                   help='name(s) of the user')

    args = parser.parse_args()

    message = args.message
    if args.name:
        message = message + ' '.join(args.name)
    if args.capitals:
        names = names.upper()
    print(f"{message} {names}")


### Where to learn more?

[https://docs.python.org/3/howto/argparse.html](https://docs.python.org/3/howto/argparse.html)
