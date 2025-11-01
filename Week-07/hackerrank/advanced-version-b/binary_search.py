#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'binary_search' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def binary_search(nums, target):
    if not nums:
        return -1

    mid = len(nums) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        result = binary_search(nums[:mid], target)
        return mid + 1 + result if result != -1 else -1
    else:
        result = binary_search(nums[mid+1:], target)
        return mid + 1 + result if result != -1 else -1

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_data)
    
    nums = input_list[0]
    target = input_list[1]

    result = binary_search(nums, target)
    print(result)