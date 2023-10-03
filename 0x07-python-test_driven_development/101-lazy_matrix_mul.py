#!/usr/bin/python3
"""
This module contains a function that multiplies 2 matrices.
"""


def lazy_matrix_mul(m_a, m_b):
    """
    matrix multiplication
    """
    import numpy as np
    return np.matmul(m_a, m_b)
