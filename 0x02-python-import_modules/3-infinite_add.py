#!/usr/bin/python3

from sys import argv as args


def infinite_add():
    return sum([int(x) for x in args[1:]])


if __name__ == "__main__":
    print(infinite_add())
