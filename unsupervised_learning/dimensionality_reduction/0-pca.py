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
    # Calculate SVD of centered data
    U, S, Vh = np.linalg.svd(X, full_matrices=False)
    
    # Calculate variance ratios
    variance_ratios = (S ** 2) / (S ** 2).sum()
    
    # Calculate cumulative variance ratio
    cumulative_variance_ratio = np.cumsum(variance_ratios)
    
    # Find number of components needed
    n_components = np.argmax(cumulative_variance_ratio >= var) + 1
    
    # Return the weight matrix W (transpose of first n_components of Vh)
    W = Vh[:n_components].T

    return W
