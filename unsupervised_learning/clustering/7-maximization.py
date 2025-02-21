#!/usr/bin/env python3
import numpy as np

def maximization(X, g):
    """
    Calculates the maximization step in the EM algorithm for a GMM.
    
    Parameters:
    - X: numpy.ndarray of shape (n, d) containing the dataset.
    - g: numpy.ndarray of shape (k, n) containing the posterior probabilities
         for each data point for each cluster.
    
    Returns:
    - pi: numpy.ndarray of shape (k,) containing the updated priors for each cluster.
    - m: numpy.ndarray of shape (k, d) containing the updated centroid means for each cluster.
    - S: numpy.ndarray of shape (k, d, d) containing the updated covariance matrices for each cluster.
    If an error occurs, returns None, None, None.
    
    Note: At most one loop is used in the computation of the covariance matrices.
    """
    # Validate inputs
    if not isinstance(X, np.ndarray) or not isinstance(g, np.ndarray):
        return None, None, None
    if X.ndim != 2 or g.ndim != 2:
        return None, None, None
    
    n, d = X.shape
    k, n_g = g.shape
    if n != n_g:
        return None, None, None
    
    # Compute the sum of responsibilities for each cluster
    g_sum = np.sum(g, axis=1)  # Shape: (k,)
    if np.any(g_sum == 0):
        return None, None, None
    
    # Updated priors: pi_i = sum_j(g[i, j]) / n
    pi = g_sum / n
    
    # Updated means: m_i = sum_j(g[i, j] * X[j]) / sum_j(g[i, j])
    m = np.dot(g, X) / g_sum[:, None]
    
    # Updated covariance matrices: S_i = sum_j(g[i, j] * (X[j] - m_i) (X[j] - m_i)^T) / sum_j(g[i, j])
    S = np.zeros((k, d, d))
    for i in range(k):  # Allowed: one loop over clusters
        diff = X - m[i]          # Shape: (n, d)
        weighted_diff = diff * g[i, :][:, None]  # Weight each row by the corresponding posterior
        S[i] = np.dot(weighted_diff.T, diff) / g_sum[i]
    
    return pi, m, S
