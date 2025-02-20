#!/usr/bin/env python3
"""Module for Poisson distribution class"""


class Poisson:
    """Class that represents a poisson distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize Poisson distribution
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
            self.lambtha = float(sum(data) / len(data))

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes
        Args:
            k: number of successes
        Returns:
            PMF value for k
        """
        if k < 0:
            return 0
        k = int(k)
        
        # Calculate k factorial
        factorial = 1
        for i in range(1, k + 1):
            factorial *= i
            
        # Calculate PMF: (λ^k * e^(-λ)) / k!
        e = 2.7182818285
        numerator = (self.lambtha ** k) * (e ** -self.lambtha)
        return numerator / factorial

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of successes
        Args:
            k: number of successes
        Returns:
            CDF value for k
        """
        if k < 0:
            return 0
        k = int(k)
        
        # Sum up PMF from 0 to k
        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
            
        return cdf
