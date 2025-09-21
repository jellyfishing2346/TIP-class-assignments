#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'rotate_matrix' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY matrix as parameter.
#

def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
   
    return matrix

if __name__ == '__main__':
    input_str = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_str)
    result = rotate_matrix(input_list)
    print(result)
