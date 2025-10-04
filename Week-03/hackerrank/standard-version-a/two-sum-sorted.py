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
#  1. INTEGER_ARRAY numbers
#  2. INTEGER target
#

def two_sum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # Convert to 1-based indices
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    for line in input_data:
        input_list = ast.literal_eval(line)
        nums = input_list[0]
        target = input_list[1]

        result = two_sum(nums, target)
        outfile.write(str(result) + '\n')
    outfile.close()