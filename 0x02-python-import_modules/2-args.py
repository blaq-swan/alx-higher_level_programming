#!/usr/bin/python3

from sys import argv as args


def commandline_args():
    if len(args) < 2:
        print("{} arguments.".format(0))
    elif len(args) == 2:
        print("{} argument:".format(len(args[1:])))
        for count, arg in enumerate(args[1:], start=1):
            print("{}: {}".format(count, arg))
    else:
        print("{} arguments:".format(len(args[1:])))
        for count, arg in enumerate(args[1:], start=1):
            print("{}: {}".format(count, arg))


if __name__ == "__main__":
    commandline_args()
