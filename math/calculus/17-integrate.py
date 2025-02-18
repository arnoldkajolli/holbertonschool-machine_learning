#!/usr/bin/env python3
"""
17-integrate.py

This module provides a function poly_integral that calculates the integral of a
polynomial represented as a list of coefficients. The index of the list
represents the power of x that the coefficient belongs to. For example, if
    f(x) = x^3 + 3x + 5,
then poly is [5, 3, 0, 1]. C is an integer representing the integration
constant. If a coefficient is a whole number, it is represented as an integer.
If poly or C are not valid, the function returns None. The returned list of
coefficients is as small as possible (trailing zeros removed).
"""


def poly_integral(poly, C=0):
    """
    Calculates the integral of a polynomial.

    Parameters:
        poly (list): A list of coefficients representing a polynomial, where
            the index corresponds to the power of x.
        C (int): An integer representing the integration constant.

    Returns:
        list: A new list of coefficients representing the integral of the
            polynomial. The constant of integration is at index 0. If poly or C
            is not valid, returns None.
    """
    if not isinstance(poly, list) or not isinstance(C, (int, float)):
        return None
    if len(poly) == 0:
        return None
    if not all(isinstance(coef, (int, float)) for coef in poly):
        return None

    result = [C]
    # Compute the integrated coefficients:
    # For each coefficient poly[i], the integrated coefficient is calculated as
    # poly[i] divided by (i + 1).
    for i, coef in enumerate(poly):
        integrated_coef = coef / (i + 1)
        # Represent whole numbers as int.
        if integrated_coef == int(integrated_coef):
            integrated_coef = int(integrated_coef)
        result.append(integrated_coef)

    # Trim trailing zeros but ensure that at least one coefficient remains.
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


if __name__ == '__main__':
    # Expected output for main_3.py: [0, 5, 1.5, 0, 0.25]
    print(poly_integral([5, 3, 0, 1]))
    # For testing a constant polynomial (as in main_4.py):
    # With default C=0, expected output: [0, 5]
    print(poly_integral([5]))
    # With C=7, expected output: [7, 5]
    print(poly_integral([5], 7))
