#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'count_pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def count_pairs(nums, target):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] < target:
                count += 1
    return count

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        # Convert the line to list of lists
        nums, target = eval(line)
        result = count_pairs(nums, target)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()