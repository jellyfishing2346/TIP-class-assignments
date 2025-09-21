#!/bin/python

import math
import os
import random
import re
import sys
import ast



# Complete the 'valid_mountain_array' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def valid_mountain_array(arr):
    # Write your code here
    n = len(arr)
    if n < 3:
        return False
    i = 0
    # walk up
    while i + 1 < n and arr[i] < arr[i + 1]:
        i += 1
    # peak can't be first or last
    if i == 0 or i == n - 1:
        return False
    # walk down
    while i + 1 < n and arr[i] > arr[i + 1]:
        i += 1
    return i == n - 1

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip()

    matches = re.findall(r'\[.*?\]', input_data)

    for arr_str in matches:
        arr = ast.literal_eval(arr_str)

        result = valid_mountain_array(arr)

        outfile.write(str(result) + '\n')
    outfile.close()