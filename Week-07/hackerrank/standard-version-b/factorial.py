#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        nums = ast.literal_eval(line.strip())   
        result = factorial(nums)
        outfile.write(str(result) + '\n')
    outfile.close()
