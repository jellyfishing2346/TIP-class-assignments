#!/bin/python

import math
import os
import random
import re
import sys
import ast
import json



#
# Complete the 'subarray_sum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER k
#

def subarray_sum(nums, k):
    count = 0
    prefix_sum = 0
    prefix_map = {0: 1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum - k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    return count

    # Write your code here

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        parts = json.loads(f"[{line}]")
        nums = parts[0]
        k = parts[1]
        result = subarray_sum(nums, k)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()