#!/usr/bin/env python3
"""
Maximization step of the EM algorithm for GMM
"""
import numpy as np


def maximization(X, g):
    """
    Performs the maximization step in the EM algorithm for a Gaussian Mixture Model.

    Parameters:
        X (numpy.ndarray): Data set of shape (n, d) where n is the number of samples
                           and d is the number of features.
        g (numpy.ndarray): Posterior probabilities of shape (k, n) where k is the number
                           of clusters and n is the number of samples.

    Returns:
        pi (numpy.ndarray): Updated priors of shape (k,).
        m (numpy.ndarray): Updated centroid means of shape (k, d).
        S (numpy.ndarray): Updated covariance matrices of shape (k, d, d).

        Returns (None, None, None) on failure.
    """
    # Validate inputs
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None
    if not isinstance(g, np.ndarray) or g.ndim != 2:
        return None, None, None

    n, d = X.shape
    k, n_g = g.shape
    if n != n_g:
        return None, None, None

    # Check that posterior probabilities for each sample sum to 1
    if not np.allclose(np.sum(g, axis=0), 1):
        return None, None, None

    # Calculate the sum of posterior probabilities for each cluster
    g_sum = np.sum(g, axis=1)  # Shape: (k,)
    if np.any(g_sum == 0):
        return None, None, None

    # Compute updated priors (pi)
    pi = g_sum / n

    # Compute updated means (m)
    m = np.dot(g, X) / g_sum[:, None]

    # Compute updated covariance matrices (S) using a single loop over clusters
    S = np.zeros((k, d, d))
    for i in range(k):
        diff = X - m[i]  # Shape: (n, d)
        # Weight the differences by the posterior probabilities and compute the covariance
        S[i] = np.dot((g[i][:, None] * diff).T, diff) / g_sum[i]

    return pi, m, S
