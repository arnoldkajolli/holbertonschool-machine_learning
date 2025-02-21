#!/usr/bin/env python3
"""
Module containing function for PCA
"""
import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where:
            n is the number of data points
            d is the number of dimensions in each point
            all dimensions have a mean of 0 across all data points
        var: fraction of the variance that the PCA transformation should maintain

    Returns:
        W: numpy.ndarray of shape (d, nd) where nd is the new dimensionality
           of the transformed X, containing the weights matrix
    """
    # Calculate covariance matrix
    covariance = np.matmul(X.T, X) / X.shape[0]

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)

    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Calculate cumulative sum of variance ratios
    cumsum = np.cumsum(eigenvalues) / np.sum(eigenvalues)

    # Find number of components needed to maintain desired variance
    r = np.argwhere(cumsum >= var)[0, 0]

    # Return weights matrix W with selected components
    W = eigenvectors[:, :(r + 1)]

    return W