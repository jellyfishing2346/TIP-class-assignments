#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'find_kth_positive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER k
#

def find_kth_positive(arr, k):
    # Write your code here
    missing = []
    current = 1
    i = 0

    while len(missing) < k:
        if i < len(arr) and arr[i] == current:
            i += 1
        else:
            missing.append(current)
        current += 1

    return missing[-1]


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        arr, k = eval(line)
        result = find_kth_positive(arr, k)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()