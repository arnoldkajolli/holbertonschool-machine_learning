#!/usr/bin/env python3
"""Contains a function that performs elementwise operations on numpy.ndarrays"""


def np_elementwise(mat1, mat2):
    """
    Performs elementwise addition, subtraction, multiplication, and division
    Args:
        mat1: First numpy.ndarray
        mat2: Second numpy.ndarray
    Returns:
        Tuple containing the elementwise sum, difference, product, and quotient
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
