#!/usr/bin/env python3
"""
Main file to test PCA on MNIST data loaded directly from online URLs.
"""

import numpy as np
import urllib.request
from io import StringIO
pca = __import__('0-pca').pca


def load_data(url, dtype=float):
    """
    Loads data from an online text file.

    Args:
        url: URL to the text file.
        dtype: Data type for the loaded data.

    Returns:
        numpy.ndarray containing the loaded data.
    """
    with urllib.request.urlopen(url) as response:
        data = response.read().decode('utf-8')
    return np.loadtxt(StringIO(data), dtype=dtype)


# URLs for the dataset and labels
X_url = "https://intranet-projects-files.s3.amazonaws.com/holbertonschool-ml/mnist2500_X.txt"
labels_url = ("https://s3.eu-west-3.amazonaws.com/hbtn.intranet/uploads/text/2019/10/"
              "72a86270e2a1c2cbc14b.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&"
              "X-Amz-Credential=AKIA4MYA5JM5DUTZGMZG%2F20250221%2Feu-west-3%2Fs3%2Faws4_request&"
              "X-Amz-Date=20250221T134416Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&"
              "X-Amz-Signature=0b080ce950e8ad70798a4c55fee7806220dc1a564e144af83d0b85824fc266d3")

# Load data from the URLs
X = load_data(X_url)
labels = load_data(labels_url, dtype=int)

# Center the data (each feature/column will have a mean of 0)
X_m = X - np.mean(X, axis=0)

# Compute the PCA weights matrix (retain at least 95% of the variance)
W = pca(X_m, var=0.95)

# Transform the data using the PCA weights matrix
T = np.matmul(X_m, W)

# Optionally, reconstruct the data to compute the reconstruction error
X_t = np.matmul(T, W.T)
error = np.sum(np.square(X_m - X_t)) / X_m.shape[0]
