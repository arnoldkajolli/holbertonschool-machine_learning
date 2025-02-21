#!/usr/bin/env python3
"""
Module containing function for PCA transformation
"""
import numpy as np


def pca(X, ndim):
    """
    Performs PCA on a dataset to reduce dimensions.

    Args:
        X: numpy.ndarray of shape (n, d) where:
            n is the number of data points
            d is the number of dimensions in each point
        ndim: new dimensionality of the transformed X

    Returns:
        T: numpy.ndarray of shape (n, ndim) containing the transformed version of X
    """
    # Center the data by subtracting the mean
    X_mean = X - np.mean(X, axis=0)

    # Compute SVD
    U, S, Vh = np.linalg.svd(X_mean, full_matrices=False)

    # Get the first ndim principal components
    W = Vh.T[:, :ndim]

    # Transform the data
    T = np.matmul(X_mean, W)

    return T
