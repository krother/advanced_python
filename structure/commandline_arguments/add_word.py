#! /usr/bin/env python3

import sys

if len(sys.argv) < 3:
    print("usage: add_word.py <filename> <suffix>")
    sys.exit(0)

filename = sys.argv[1]
suffix = sys.argv[2]

for line in open(filename):
    prefix = line.strip()
    result = prefix + " with " + suffix
    print(result)
