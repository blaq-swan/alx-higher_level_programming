#!/usr/bin/python3
"""module 12"""


def pascal_triangle(n):
    """pascal triangle"""

    if n <= 0:
        return []

    triangle = [[1]]

    while len(triangle) != n:
        x = triangle[-1]
        y = [1]

        for a in range(len(x) - 1):
            y.append(x[a] + x[a + 1])
        y.append(1)
        triangle.append(y)
    return triangle
