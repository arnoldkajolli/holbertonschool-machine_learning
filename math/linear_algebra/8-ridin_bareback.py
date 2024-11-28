#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication of two matrices.
    Args:
        mat1: First matrix (2D list of ints/floats)
        mat2: Second matrix (2D list of ints/floats)
    Returns:
        New matrix containing the product, or None if matrices cannot be multiplied
    """
    # Check if matrices can be multiplied
    if not mat1 or not mat2 or not mat1[0] or not mat2[0]:
        return None
    
    # Get dimensions
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    
    # Check if multiplication is possible
    if cols1 != rows2:
        return None
        
    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    
    # Perform matrix multiplication
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
                
    return result
