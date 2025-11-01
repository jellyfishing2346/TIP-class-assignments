#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'find_peak_element' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def find_peak_element(nums):
    # Accept either a Python list or a string representation of a list.
    if nums is None:
        return -1

    # If input is a string, try to parse it as a Python literal
    if isinstance(nums, str):
        try:
            nums_list = ast.literal_eval(nums)
        except Exception:
            # fallback: extract integers from the string
            nums_list = [int(x) for x in re.findall(r'-?\d+', nums)]
    else:
        nums_list = nums

    if not nums_list:
        return -1

    # Binary search for a peak element (O(log n))
    lo, hi = 0, len(nums_list) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums_list[mid] > nums_list[mid + 1]:
            # peak is in left half including mid
            hi = mid
        else:
            # peak is in right half excluding mid
            lo = mid + 1
    return lo


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        nums = line.strip().strip('"')  
        result = find_peak_element(nums)
        outfile.write(str(result) + '\n')
    outfile.close()

