#!/usr/bin/env python3
"""Module for Normal distribution class"""

import math


class Normal:
    """Class that represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize Normal distribution.
        Args:
            data: list of data to estimate distribution
            mean: mean of the distribution
            stddev: standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / (len(data) - 1)
            self.stddev = math.sqrt(variance)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value.
        Args:
            x: x-value
        Returns:
            z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score.
        Args:
            z: z-score
        Returns:
            x-value corresponding to z
        """
        return self.mean + z * self.stddev

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value.
        Args:
            x: x-value
        Returns:
            PDF value for x
        """
        pi = math.pi
        e = math.e
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2
        coefficient = 1 / (self.stddev * math.sqrt(2 * pi))
        return coefficient * (e ** exponent)

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.
        Uses a common polynomial approximation.
        Args:
            x: x-value
        Returns:
            CDF value for x
        """
        z = (x - self.mean) / self.stddev
        t = 1 / (1 + 0.2316419 * abs(z))
        poly = (0.31938153 * t -
                0.356563782 * t ** 2 +
                1.781477937 * t ** 3 -
                1.821255978 * t ** 4 +
                1.330274429 * t ** 5)
        approx = (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * z ** 2) * poly
        if z >= 0:
            cdf = 1 - approx
        else:
            cdf = approx
        return cdf
