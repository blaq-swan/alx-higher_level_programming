#!/usr/bin/python3
"""module for is_same_class"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class
    Args:
        obj: object to be checked
        a_class: class reference
    """
    return True if type(obj) == a_class else False
