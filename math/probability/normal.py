#!/usr/bin/env python3
"""Module for Normal distribution class"""


class Normal:
    """Class that represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Initialize Normal distribution
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

            # Calculate mean
            self.mean = float(sum(data) / len(data))

            # Calculate standard deviation
            squared_diff_sum = sum(
                [(x - self.mean) ** 2 for x in data]
            )
            self.stddev = float((squared_diff_sum / len(data)) ** 0.5)

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value
        Args:
            x: x-value
        Returns:
            z-score of x
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score
        Args:
            z: z-score
        Returns:
            x-value of z
        """
        return self.mean + (z * self.stddev)

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value
        Args:
            x: x-value
        Returns:
            PDF value for x
        """
        pi = 3.1415926536
        e = 2.7182818285

        # Calculate exponent term: -(x-μ)²/(2σ²)
        exponent = -0.5 * ((x - self.mean) / self.stddev) ** 2

        # Calculate coefficient: 1/(σ√(2π))
        coefficient = 1 / (self.stddev * (2 * pi) ** 0.5)

        return coefficient * (e ** exponent)
