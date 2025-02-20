#!/usr/bin/env python3
"""Module for Binomial distribution class"""


class Binomial:
    """Class that represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize Binomial distribution
        Args:
            data: list of data to estimate distribution
            n: number of Bernoulli trials
            p: probability of success
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError(
                    "p must be greater than 0 and less than 1"
                )
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")

            # Calculate mean and variance of the data
            mean = sum(data) / len(data)
            variance = sum(
                (x - mean) ** 2 for x in data
            ) / len(data)

            # Calculate p first (p = 1 - variance/mean)
            self.p = float(1 - (variance / mean))

            # Calculate n (n = mean/p)
            self.n = round(mean / self.p)

            # Recalculate p using the rounded n
            self.p = float(mean / self.n)
