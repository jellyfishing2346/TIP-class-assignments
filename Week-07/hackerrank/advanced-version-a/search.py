#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'search' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def search(nums, target):
    # Handle edge cases
    if nums is None:
        return -1
    n = len(nums)
    if n == 0:
        return -1

    lo, hi = 0, n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid

        # Determine which side is sorted
        if nums[lo] <= nums[mid]:
            # left half [lo..mid] is sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            # right half [mid..hi] is sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1

    return -1


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        nums, target = eval(line)
        result = search(nums, target)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()
