#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    power = []

    for x in matrix:
        power.append([pow(y, 2) for y in x])
    return power
