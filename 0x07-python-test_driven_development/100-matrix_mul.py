#!/usr/bin/python3
" matrix multiplication"


def matrix_mul(m_a, m_b):
    """multiply two matrices
    m_a and m_b are lists of lists of integers
    Raises:
        TypeError: if not maytix of ints or matrix rows are not equal
        ValueError: if either matrix is empty or if they cant be multiplied
    Return:
        The resulting matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(x, (int, float))
                for x in [n for row in m_a for n in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float))
                for x in [n for row in m_b for n in row]):
        raise TypeError("m_b should contain only integers of floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = []
    for row in range(len(m_a)):
        cur = []
        for col in range(len(m_b[0])):
            cur.append(0)
        res.append(cur)

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                res[i][j] += m_a[i][k] * m_b[k][j]
    return res
