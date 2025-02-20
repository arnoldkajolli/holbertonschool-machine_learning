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

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of "successes"
        Args:
            k: number of successes
        Returns:
            PMF value for k
        """
        k = int(k)

        if k < 0 or k > self.n:
            return 0

        # Calculate n choose k (combinations formula)
        n_factorial = 1
        for i in range(1, self.n + 1):
            n_factorial *= i

        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i

        nk_factorial = 1
        for i in range(1, self.n - k + 1):
            nk_factorial *= i

        combinations = n_factorial / (k_factorial * nk_factorial)

        # Calculate PMF: C(n,k) * p^k * (1-p)^(n-k)
        return combinations * (self.p ** k) * ((1 - self.p) ** (self.n - k))

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of "successes"
        Args:
            k: number of successes
        Returns:
            CDF value for k
        """
        k = int(k)

        if k < 0:
            return 0

        # CDF is sum of PMF from 0 to k
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)

        return cdf
