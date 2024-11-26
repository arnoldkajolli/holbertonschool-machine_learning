#!/usr/bin/env python3
""" a script that adds two arrays  """


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis
    axis=0 means vertically (add rows)
    axis=1 means horizontally (add columns)
    """
    # Create deep copy of matrices to avoid modifying originals
    result = []
    
    # For vertical stacking (axis=0)
    if axis == 0:
        # Check if matrices have same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None
        
        # Copy mat1's rows
        for row in mat1:
            result.append(row[:])
        # Add mat2's rows
        for row in mat2:
            result.append(row[:])
            
    # For horizontal stacking (axis=1)
    elif axis == 1:
        # Check if matrices have same number of rows
        if len(mat1) != len(mat2):
            return None
            
        # Concatenate each row
        for i in range(len(mat1)):
            result.append(mat1[i][:] + mat2[i][:])
            
    return result
