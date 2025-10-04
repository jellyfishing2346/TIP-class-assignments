#!/bin/python3

import math
import os
import random
import re
import sys
import ast
import json



#
# Complete the 'array_rank_transform' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def array_rank_transform(arr):
    # Get unique elements and sort them
    sorted_unique = sorted(set(arr))
    
    # Create a mapping from value to rank (1-based)
    rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
    
    # Transform the original array using the rank mapping
    return [rank_map[num] for num in arr]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().split('\n')
    
    for line in input_lines:
        if line:  # Check if the line is not empty
            arr = json.loads(line)  # Parse the line as JSON
            result = array_rank_transform(arr)
            outfile.write(str(result) + '\n')
    outfile.close()