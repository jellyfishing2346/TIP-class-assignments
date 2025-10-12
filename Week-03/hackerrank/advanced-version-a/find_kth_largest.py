#!/bin/python

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'find_kth_largest' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        # Convert the line to list of lists
        nums, k = eval(line)
        result = find_kth_largest(nums, k)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()
