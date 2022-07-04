#!/usr/bin/python3
"""class module"""


def inherits_from(obj, a_class):
    """checks if obj inherited from a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
