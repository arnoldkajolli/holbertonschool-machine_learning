#!/usr/bin/env python3
""" A script that returns the transpose of a 2D matrix"""


def matrix_transpose(matrix):
   rows = len(matrix[0])
   cols = len(matrix)
   result = [[0 for _ in range(cols)] for _ in range(rows)]
   
   for i in range(rows):
       for j in range(cols):
           result[i][j] = matrix[j][i]
           
   return result
