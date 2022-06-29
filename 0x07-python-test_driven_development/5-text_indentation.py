#!/usr/bin/python3
"""module for text_indentation method"""


def text_indentation(text):
    """Adds two lines after :?.

    Args:
        text: source string

    Raises:
        TypeError: if text is not a string

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        text = (delimeter + "\n" * 2).join(
            [line.strip(" ") for line in text.split(delimeter)]
            )

    print(text, end="")
