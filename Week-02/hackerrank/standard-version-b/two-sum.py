#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'two_sum' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums
#  2. INTEGER target
#

def two_sum(nums, target):
    # Write your code here
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1, -1]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip()
    
    # Split the input data by newlines
    input_cases = input_data.splitlines()
    
    for input_case in input_cases:
        # Each case should be parsed into a tuple or list
        input_list = ast.literal_eval(input_case)

        # Extract nums and target from input_list
        nums = input_list[0]
        target = input_list[1]

        # Get the result from the two_sum function
        result = two_sum(nums, target)
        outfile.write(str(result) + '\n')
    outfile.close()