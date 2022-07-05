#!/usr/bin/python3
"""module 9"""


class Student:
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """constructor"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """namespace for cls Student"""
        return self.__dict__
