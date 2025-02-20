#!/usr/bin/env python3
"""Module for Exponential distribution class"""


class Exponential:
    """Class that represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize Exponential distribution
        Args:
            data: list of data to estimate distribution
            lambtha: expected number of occurrences
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period
        Args:
            x: time period
        Returns:
            PDF value for x
        """
        if x < 0:
            return 0
        e = 2.7182818285  # Euler's number
        return self.lambtha * (e ** (-self.lambtha * x))
