#!/usr/bin/python3
"""file reader"""


def append_write(filename="", text=""):
    """appends into a file"""

    with open(filename, "a", encoding="utf-8") as file:
        return (file.write(text))
