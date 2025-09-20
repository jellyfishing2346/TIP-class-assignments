#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'check_list' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_ARRAY nums as parameter.
#

def check_list(nums):
    x = len(nums)
    sum_count = sum(1 for n in nums if n >= x)
    return sum_count >= x

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":   
            continue
        
        try:
            nums = ast.literal_eval(input_str)
    
            result = check_list(nums)
 
            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")
    outfile.close()