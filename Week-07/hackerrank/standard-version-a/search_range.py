#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'search_range' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def search_range(nums, target):
    # Write your code here
    def find_first(nums, target):
        id = -1
        low, high = 0, len(nums) - 1
    
        while low <= high:
            middle = (low + high) // 2
            
            if nums[middle] == target:
                id = middle
                high = middle - 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
    
        return id
    
    def find_last(nums, target):
        id = -1
        low, high = 0, len(nums) - 1
    
        while low <= high:
            middle = (low + high) // 2
            
            if nums[middle] == target:
                id = middle
                low = middle + 1
            elif nums[middle] < target:
                low = middle + 1
            else:
                high = middle - 1
    
        return id
    
    first = find_first(nums, target)
    last = find_last(nums, target)
    
    return [first, last]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        nums, target = eval(line)
        result = search_range(nums, target)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()