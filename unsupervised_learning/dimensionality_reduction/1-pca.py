#!/usr/bin/env python3
"""
Module containing function for PCA transformation
"""
import numpy as np


def pca(X, ndim):
    """
    Performs PCA on a dataset to reduce dimensions.
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
