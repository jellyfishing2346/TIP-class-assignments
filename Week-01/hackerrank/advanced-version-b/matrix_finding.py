#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'find_value_index' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY matrix
#  2. INTEGER value
#

def find_value_index(matrix, value):
    # Write your code here
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                return [i, j]
    return [-1, -1]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')

    input_data = sys.stdin.read().strip()
    
    # Separate matrix and value parts
    matrix_match = re.search(r'matrix\s*=\s*(\[\[.*?\]\])', input_data, re.DOTALL)
    value_match = re.search(r'value\s*=\s*(\d+)', input_data)
    
    if matrix_match and value_match:
        matrix_str = matrix_match.group(1)
        value = int(value_match.group(1))
        
        # Convert matrix string to list of lists
        matrix = eval(matrix_str)
        
        # Finding value index
        result = find_value_index(matrix, value)
        
        outfile.write(str(result) + '\n')
    else:
        outfile.write(str([-1, -1]) + '\n')
    outfile.close()