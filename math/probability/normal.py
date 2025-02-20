#!/usr/bin/env python3
"""Module for Binomial distribution class"""

class Binomial:
    """Class that represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Initialize Binomial distribution.

        Args:
            data: list of data to estimate distribution
            n: number of Bernoulli trials
            p: probability of a "success"

        If data is not given:
            Use the provided n and p.
            - If n is not a positive value, raise a ValueError with the message
              n must be a positive value
            - If p is not a valid probability, raise a ValueError with the message
              p must be greater than 0 and less than 1

        If data is provided:
            - If data is not a list, raise a TypeError with the message data must be a list
            - If data does not contain at least two data points, raise a ValueError with the message
              data must contain multiple values
            - Calculate p first as:
                p_initial = 1 - (variance / mean)
              where variance is computed using the population formula (dividing by len(data))
            - Calculate n as the rounded value of (mean / p_initial)
            - Recalculate p as (mean / n)
        """
        if data is None:
            if n <= 0:
                raise ValueError("n must be a positive value")
            if p <= 0 or p >= 1:
                raise ValueError("p must be greater than 0 and less than 1")
            self.n = int(n)
            self.p = float(p)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean_data = sum(data) / len(data)
            s = 0
            for x in data:
                s += (x - mean_data) ** 2
            variance = s / len(data)
            p_initial = 1 - (variance / mean_data)
            n_calc = round(mean_data / p_initial)
            p_calc = mean_data / n_calc
            self.n = int(n_calc)
            self.p = float(p_calc)
