#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'longest_subarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER limit
#

def longest_subarray(nums, limit):
    from collections import deque
    max_d = deque()
    min_d = deque()
    left = 0
    res = 0
    for right, num in enumerate(nums):
        while max_d and num > max_d[-1]:
            max_d.pop()
        max_d.append(num)
        while min_d and num < min_d[-1]:
            min_d.pop()
        min_d.append(num)
        while max_d[0] - min_d[0] > limit:
            if nums[left] == max_d[0]:
                max_d.popleft()
            if nums[left] == min_d[0]:
                min_d.popleft()
            left += 1
        res = max(res, right - left + 1)
    return res

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        nums, limit = eval(line)
        result = longest_subarray(nums, limit)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()

