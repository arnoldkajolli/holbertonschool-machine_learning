#!/usr/bin/env python3
"""
Maximization step of the EM algorithm for GMM
"""
import numpy as np


def maximization(X, g):
    """
    Calculates the maximization step in the EM algorithm for a GMM
    """
    if not isinstance(X, np.ndarray) or len(X.shape) != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or len(g.shape) != 2:
        return None, None, None
    if X.shape[0] != g.shape[1]:
        return None, None, None

    n, d = X.shape
    k = g.shape[0]

    # Sum of posterior probabilities should be 1
    if not np.isclose(np.sum(g, axis=0), np.ones(n)).all():
        return None, None, None

    try:
        # Calculate new priors (pi)
        pi = np.sum(g, axis=1) / n

        # Calculate new means (m)
        m = np.dot(g, X) / np.sum(g, axis=1).reshape(-1, 1)

        # Calculate new covariance matrices (S)
        S = np.zeros((k, d, d))
        for i in range(k):
            diff = X - m[i]
            S[i] = np.dot((g[i].reshape(-1, 1) * diff).T, diff) / np.sum(g[i])

        return pi, m, S

    except Exception:
        return None, None, None
