#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'remove_duplicates' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def remove_duplicates(nums):
    # Write your code here
    if not nums:
        return 0

    # Two pointers
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            nums = ast.literal_eval(input_str)

            result = remove_duplicates(nums)

            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")