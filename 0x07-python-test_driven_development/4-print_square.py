#!/usr/bin/python3
"""module to print a square"""


def print_square(size):
    """prints a square of chars #

    Args:
        size (int): size of an integer

    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size > 0:
        for x in range(size):
            print("#" * size)

# print_square(None)
