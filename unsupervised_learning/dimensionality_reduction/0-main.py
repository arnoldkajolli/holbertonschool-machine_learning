#!/usr/bin/env python3
"""
Main file to test the PCA implementation.
"""

import numpy as np
pca = __import__('0-pca').pca

# Fix the random seed for reproducibility
np.random.seed(0)

# Create three independent signals
a = np.random.normal(size=50)
b = np.random.normal(size=50)
c = np.random.normal(size=50)

# Create three additional signals that are linear combinations of the above
d = 2 * a
e = -5 * b
f = 10 * c

# Stack the signals to form the dataset: each row is a data point
X = np.array([a, b, c, d, e, f]).T

# Number of samples
m = X.shape[0]

# Center the data (each feature has mean 0)
X_m = X - np.mean(X, axis=0)

# Compute the weights matrix using PCA (retain at least 95% of the variance)
W = pca(X_m, var=0.95)

# Transform the centered data into the PCA space
T = np.matmul(X_m, W)

# Print the transformed data T and its shape.
print(T)
print(T.shape)

# For demonstration, you might want to reconstruct the data
# using the PCA weights and compute the reconstruction error.
X_t = np.matmul(T, W.T)
error = np.sum(np.square(X_m - X_t)) / m
print(X_t)
print(X_t.shape)
print(error)
