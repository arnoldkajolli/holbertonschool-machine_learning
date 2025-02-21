#!/usr/bin/env python3
"""
Module containing function for PCA.
"""

import numpy as np


def pca(X, var=0.95):
    """
    Performs PCA on a dataset.

    Args:
        X: numpy.ndarray of shape (n, d) where:
           - n is the number of data points,
           - d is the number of dimensions,
           - each feature is assumed to have zero mean.
        var: fraction of the variance that the PCA transformation should maintain.

    Returns:
        W: numpy.ndarray of shape (d, nd) where nd is the new dimensionality
           (the number of principal components required to preserve at least var of the variance).
    """
    # Compute the singular value decomposition of the centered data
    U, S, Vh = np.linalg.svd(X, full_matrices=False)

    # Compute the cumulative variance ratios
    variance_ratios = np.cumsum(S ** 2) / np.sum(S ** 2)

    # Find the minimal number of components needed to retain at least 'var' of the variance
    k = np.where(variance_ratios >= var)[0][0] + 1

    # Return the weights matrix (principal components)
    return Vh.T[:, :k]
