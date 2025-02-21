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
    # Compute Singular Value Decomposition
    U, S, Vh = np.linalg.svd(X, full_matrices=False)

    # Calculate variance ratios
    variance_ratios = np.cumsum(S ** 2) / np.sum(S ** 2)

    # Find number of components needed
    k = np.where(variance_ratios >= var)[0][0] + 1

    # Return weights matrix W (right singular vectors)
    return Vh.T[:, :k]
