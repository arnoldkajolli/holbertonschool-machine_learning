#!/usr/bin/env python3
"""
10-matisse.py

This module provides a function that calculates the derivative of a polynomial.
The polynomial is represented as a list of coefficients, where the index of
each coefficient corresponds to the power of x.
Example:
    f(x) = x^3 + 3x + 5 is represented as [5, 3, 0, 1].
If poly is not valid, the function returns None.
If the polynomial is constant, the derivative is [0].
"""


def poly_derivative(poly):
    """
    Calculates the derivative of a polynomial.

    Parameters:
        poly (list): A list of coefficients representing a polynomial.
            The index corresponds to the power of x for that coefficient.

    Returns:
        list: A list of coefficients representing the derivative of the
            polynomial. If the derivative is 0, returns [0]. If poly is not
            valid, returns None.
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if not all(isinstance(c, (int, float)) for c in poly):
        return None
    if len(poly) == 1:
        return [0]

    derivative = [(i + 1) * poly[i + 1] for i in range(len(poly) - 1)]
    return derivative


if __name__ == '__main__':
    # Example test:
    print(poly_derivative([5, 3, 0, 1]))
