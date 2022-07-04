#!/usr/bin/python3
"""module 2-is_same_class"""


def is_same_class(obj, a_class):
    """Check if obj is instance of a_class"""

    if isinstance(obj, a_class):
        return True
    return False
