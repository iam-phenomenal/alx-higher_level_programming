#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    i = 1
    if len(argv) < 2:
        print("0 arguments.")
    elif len(argv) < 3:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(len(argv) - 1))
    for arg in argv[1:]:
        print("{:d}: {:s}".format(i, arg))
        i += 1
