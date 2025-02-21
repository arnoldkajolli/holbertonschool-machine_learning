#!/usr/bin/env python3
"""
Performs PCA with specified variance retention
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
           of the transformed X
    """
    # Perform SVD on X
    _, s, vh = np.linalg.svd(X)

    # Calculate cumulative sum of explained variance ratios
    explained_variance_ratio = np.cumsum(s ** 2) / np.sum(s ** 2)

    # Find number of components needed to maintain desired variance
    n_components = np.argwhere(explained_variance_ratio >= var)[0, 0] + 1

    # Return weights matrix (right singular vectors)
    return vh.T[:, :n_components]
