#!/usr/bin/python3
"""json writer"""
from json import dump


def save_to_json_file(my_obj, filename):
    """writes a text to json representation"""

    with open(filename, 'w') as file:
        dump(my_obj, file)
