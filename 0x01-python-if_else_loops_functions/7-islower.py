#!/usr/bin/python3


def islower(c):
    string = [chr(a) for a in range(97, 123)]
    if c in string and c.isalpha():
        return True
    else:
        return False
