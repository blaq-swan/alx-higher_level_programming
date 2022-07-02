#!/usr/bin/python3
"""100-matrix module"""


def matrix_mul(m_a, m_b):
    """matrix mul func
    Args: m_a m_b
    Raises
        TypeError:
            if not a list of list
            if not of same size
            if not in (int, float)
        ValueError:
            if matrices are empty
    Return:
        m_a * m_b"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not any(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not any(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        for y in row:
            if not isinstance(y, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    dim_a, dim_b = [len(m_a)], [len(m_b)]
    for x, y in zip(m_a, m_b):
        dim_a.append(len(x))
        dim_b.append(len(y))
        break

    if dim_a[1] != dim_b[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a * b for a, b in zip(x, y)) for y in zip(*m_b)] for x in m_a]
