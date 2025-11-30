#!/usr/bin/python3
"""
Module 12-pascal_triangle
Defines a function pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev = triangle[-1]
        row = [1]

        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])

        row.append(1)
        triangle.append(row)

    return triangle
