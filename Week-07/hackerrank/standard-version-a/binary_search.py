#!/bin/python3

import math
import os
import random
import re
import sys
import ast



def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1
        
    return -1

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_data)
    
    nums = input_list[0]
    target = input_list[1]

    result = binary_search(nums, target)
    print(result)