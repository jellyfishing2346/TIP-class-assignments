#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'kthSmallest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. DOUBLE_ARRAY matrix
#  2. INTEGER k
#

def kthSmallest(matrix, k):
    flat = [num for row in matrix for num in row]
    flat.sort()
    return flat[k-1]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        # Convert the line to list of lists
        matrix, k = eval(line)
        result = kthSmallest(matrix, k)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()