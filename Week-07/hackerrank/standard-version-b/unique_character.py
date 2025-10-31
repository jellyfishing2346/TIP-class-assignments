#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'single_non_duplicate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def single_non_duplicate(nums):
    # Write your code here
    count = 0
    
    for i in nums:
        count ^= i
        
    return count

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        nums = ast.literal_eval(line.strip())  # Properly parse the list from the string
        result = single_non_duplicate(nums)
        outfile.write(str(result) + '\n')
    outfile.close()
