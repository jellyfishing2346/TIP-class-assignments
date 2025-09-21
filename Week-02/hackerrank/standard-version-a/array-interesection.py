#!/bin/python

import math
import os
import random
import re
import sys
import ast
import json


#
# Complete the 'intersection' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def intersection(nums1, nums2):
    # Use set intersection to find unique common elements, return sorted result
    return sorted(set(nums1) & set(nums2))

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().split('\n')
    
    results = []
    for line in input_lines:
        input_list = ast.literal_eval(line)
        nums1 = input_list[0]
        nums2 = input_list[1]
        
        result = intersection(nums1, nums2)
        results.append(result)
    
    for result in results:
        outfile.write(str(result) + '\n')
    outfile.close()