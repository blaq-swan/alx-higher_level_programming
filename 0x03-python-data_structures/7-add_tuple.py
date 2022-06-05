#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a, b = tuple_a, tuple_b

    if len(a) in range(2):
        if len(a) == 0:
            a = 0, 0
        else:
            a = a[0], 0
    if len(b) in range(2):
        if len(b) == 0:
            b = 0, 0
        else:
            b = b[0], 0
    return a[0] + b[0], a[1] + b[1]
