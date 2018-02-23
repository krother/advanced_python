
import argparse
import sys

if __name__ == '__main__':
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
