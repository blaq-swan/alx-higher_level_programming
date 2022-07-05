#!/usr/bin/python3
"""json loader"""
from json import loads


def from_json_string(my_str):
    """loads a json string"""

    return loads(my_str)
