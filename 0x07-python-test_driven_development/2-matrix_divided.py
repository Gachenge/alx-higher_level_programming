#!/usr/bin/python3

"""function to divide all elements of a matrix"""

def matrix_divided(matrix, div):
    """divide all elements of a matrix
    Args:
        matrix: a list of lists of integers or floats.
        div: must be integer or float
    Raises:
        TypeError - if not matrix
        TypeError - if each row not same size
        TypeError - if div is not a number
        ZeroDivisionError - if div is 0
    Returns:
        a new matrix after division
        """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(ele, list) for ele in matrix) or
            not all(isinstance(x, (int, float))
                for x in [n for ele in matrix for n in ele])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
