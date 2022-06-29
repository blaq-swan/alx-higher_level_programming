#!/usr/bin/python3
"""module to divide elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides elements of matrix with div

    Args:
        matrix: a list of list of numbers
        div: a dividend

    Raises:
        TypeError: if div is not a number
        TypeError: if matrix is not a list of list of numbers
        TypeError: if items of matrix are not of the same size
        ZeroDivisionError: if div is zero

    Returns:
        A list of lists of numbers divided by div
    """

    typerr = 'matrix must be a matrix (list of lists) of integers/floats'

    if not matrix:
        raise TypeError(typerr)

    if not isinstance(matrix, list):
        raise TypeError(typerr)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(typerr)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(typerr)
        for num in row:
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(typerr)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(x) == len(matrix[0]) for x in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(x / div, 2) for x in y] for y in matrix]
