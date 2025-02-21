#!/usr/bin/env python3
"""
Function that performs PCA on a dataset
"""
import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset.

    Parameters:
        X: numpy.ndarray of shape (n, d) where:
            n is the number of data points
            d is the number of dimensions in each point
        var: fraction of the variance that the PCA transformation should maintain

    Returns:
        W: numpy.ndarray of shape (d, nd) where:
            nd is the new dimensionality of the transformed X
    """
    # Calculate the covariance matrix
    # We don't need to subtract mean as it's already done in the input
    covariance = np.matmul(X.T, X) / X.shape[0]

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(covariance)

    # Sort eigenvalues and eigenvectors in descending order
    idx = eigenvalues.argsort()[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    # Calculate cumulative variance ratio
    total_variance = np.sum(eigenvalues)
    cumulative_variance_ratio = np.cumsum(eigenvalues) / total_variance

    # Find number of components needed to maintain desired variance
    n_components = np.argmax(cumulative_variance_ratio >= var) + 1

    # Return the weight matrix W
    W = eigenvectors[:, :n_components]

    return W
