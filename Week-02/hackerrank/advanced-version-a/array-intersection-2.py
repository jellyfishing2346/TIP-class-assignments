#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'intersect' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY nums1
#  2. INTEGER_ARRAY nums2
#

def intersect(nums1, nums2):
    from collections import Counter
    counts = Counter(nums1)
    result = []
    for num in nums2:
        if counts[num] > 0:
            result.append(num)
            counts[num] -= 1
    return sorted(result)

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()

    for line in input_data:
        if line == '':
            continue
        
        # Split the input and handle empty lists
        nums1_str, nums2_str = line.split('],[')
        nums1_str = nums1_str.strip()[1:]  # Remove leading '['
        nums2_str = nums2_str.strip()[:-1]  # Remove trailing ']'

        # Handle empty lists
        if nums1_str:
            nums1 = list(map(int, nums1_str.split(',')))
        else:
            nums1 = []
        
        if nums2_str:
            nums2 = list(map(int, nums2_str.split(',')))
        else:
            nums2 = []

        result = intersect(nums1, nums2)
        import json
        outfile.write(json.dumps(result) + '\n')
    outfile.close()