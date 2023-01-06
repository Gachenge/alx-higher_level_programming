#!/usr/bin/python3
"numpy to install numpy"
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """using numpy to multiply matrixes
    m_a and m_b must be matrices of integers
    Return:
        The resulting matrix
    """
    return (np.matmul(m_a, m_b))
