#!/usr/bin/python3
"""function that returns a list of integers"""


def pascal_triangle(n):
    """returns a list of integers representing the pascal teiangle
    returns empty list if ln <= 0
    """
    pascal = []

    for i in range(n):
        pascal.append([1] * (i + 1))
    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal
