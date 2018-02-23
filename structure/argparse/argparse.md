
# argparse

### What it is good for?

Read command-line arguments

`argparse` allows you to define command-line parameters for a Python application. The module takes care of reading the parameters into meaningful attributes, checking required arguments and generating help text. 
`argparse` is the official successor to the standard module `optparse`.

### Installed with Python by default

yes

### Example

Create a command-line interface

    import argparse
    import sys

    parser = argparse.ArgumentParser(description='A Hello World program with arguments.')

    parser.add_argument('-m', '--message', type=str, default="Hello ",
                   help='message to be written')

    parser.add_argument('-o', '--outfile', nargs='?', type=argparse.FileType('w'),
                   default=sys.stdout,
                   help="output file")

    parser.add_argument('-c', '--capitals', action="store_true",
                   help='write capitals')

    parser.add_argument('name', type=str, nargs='+',
                   help='name(s) of the user')

    args = parser.parse_args()

    message = args.message
    if args.name:
        message = message + ' '.join(args.name)
    if args.capitals: 
        message = message.upper()
    args.outfile.write(message + '\n')


### Where to learn more?

[https://docs.python.org/3/howto/argparse.html](https://docs.python.org/3/howto/argparse.html)

