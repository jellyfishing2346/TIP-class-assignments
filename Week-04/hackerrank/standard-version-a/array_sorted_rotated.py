#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_sorted_rotated' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def is_sorted_rotated(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            count += 1
    return count == 0 or count == 1


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        nums = ast.literal_eval(line.strip())  
        result = is_sorted_rotated(nums)
        outfile.write(str(result) + '\n')
    outfile.close()