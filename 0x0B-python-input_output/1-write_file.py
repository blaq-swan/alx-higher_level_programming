#!/usr/bin/python3
"""file reader"""


def write_file(filename="", text=""):
    """wriites a file"""

    with open(filename, "w", encoding="utf-8") as file:
        return (file.write(text))
