#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'find_min_index_of_repeating' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def find_min_index_of_repeating(arr):
    index_map = {}
    min_index = len(arr)
    for idx, val in enumerate(arr):
        if val in index_map:
            min_index = min(min_index, index_map[val])
        else:
            index_map[val] = idx
    return min_index if min_index != len(arr) else None

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()

    for line in input_data:
        try:
            arr = ast.literal_eval(line.strip())
            result = find_min_index_of_repeating(arr)
            outfile.write(str(result) + '\n')
            # outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Invalid input")
    outfile.close()