#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'contains_duplicate' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def contains_duplicate(nums):
    # Write your code here
    is_duplicated = False
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                is_duplicated = True
    return is_duplicated

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip()
    
    lines = input_data.splitlines()

    for line in lines:
        arr = ast.literal_eval(line.strip())  

        result = contains_duplicate(arr)
        outfile.write(str(result) + '\n')
    outfile.close()