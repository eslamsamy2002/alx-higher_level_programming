#!/usr/bin/python3
"""Matrix multiplication using the module NumPy"""

from numpy import matmul


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul multiplies two matrices:
        m_a * m_b
    Arges:
        m_a: list
        m_b: list
    """
    return matmul(m_a, m_b)
