#!/usr/bin/python3
"""module 9"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """namespace for cls Student"""

        if type(attrs) == list and all(type(x) for x in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
