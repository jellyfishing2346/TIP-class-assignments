#!/bin/python

import math
import os
import random
import re
import sys
import ast



# Enter your code here. Read input from STDIN. Print output to STDOUT#
# Complete the 'valid_mtn_arr' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def valid_mtn_arr(arr):
    # Write your code here
    n = len(arr)
    if n < 3:
        return False
    i = 0
    # Ascend to the peak
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    # Peak can't be first or last
    if i == 0 or i == n - 1:
        return False
    # Descend from the peak
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    # If we reached the end, it's a valid mountain array
    return i == n - 1

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        arr = ast.literal_eval(line.strip())   
        result = valid_mtn_arr(arr)
        outfile.write(str(result) + '\n')
    outfile.close()