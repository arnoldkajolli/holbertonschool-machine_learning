#!/usr/bin/env python3
"""
9-sum_total.py
This module provides a function that calculates the sum of squares from 1 to n
without using any loops.
"""

def summation_i_squared(n):
    """
    Calculates the sum of squares from 1 to n.

    The function computes the sum:
        1^2 + 2^2 + ... + n^2
    using the formula:
        n*(n+1)*(2*n+1) // 6

    Parameters:
        n (int): The stopping condition. Must be a positive integer.

    Returns:
        int: The sum of squares from 1 to n.
        None: If n is not a valid positive integer.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6

if __name__ == '__main__':
    # Optional: quick test when running the module directly.
    print(summation_i_squared(5))
