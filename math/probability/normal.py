#!/usr/bin/env python3
"""Module for Normal distribution class"""

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
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.mean = float(sum(data) / len(data))
            # Use the unbiased estimator: divide by (n - 1)
            variance = 0
            for x in data:
                variance += (x - self.mean) ** 2
            variance = variance / (len(data) - 1)
            self.stddev = variance ** 0.5

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
        PI = 3.1415926536
        E = 2.7182818285
        exponent = -0.5 * (((x - self.mean) / self.stddev) ** 2)
        coefficient = 1 / (self.stddev * (2 * PI) ** 0.5)
        return coefficient * (E ** exponent)

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value.
        Uses a common polynomial approximation.
        Args:
            x: x-value
        Returns:
            CDF value for x
        """
        PI = 3.1415926536
        E = 2.7182818285
        z = (x - self.mean) / self.stddev
        t = 1 / (1 + 0.2316419 * (abs(z)))
        poly = (0.31938153 * t -
                0.356563782 * t ** 2 +
                1.781477937 * t ** 3 -
                1.821255978 * t ** 4 +
                1.330274429 * t ** 5)
        approx = (1 / (2 * PI) ** 0.5) * (E ** (-0.5 * z ** 2)) * poly
        if z >= 0:
            cdf = 1 - approx
        else:
            cdf = approx
        return cdf
