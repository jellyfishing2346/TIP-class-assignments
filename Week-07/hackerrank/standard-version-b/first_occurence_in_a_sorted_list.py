#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'find_first_occurrence' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY names
#  2. STRING val
#

def find_first_occurrence(names, val):
    # Write your code here
    for i, ch in enumerate(names):
        if ch == val:
            return i
    return -1


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        names, val = eval(line)
        result = find_first_occurrence(names, val)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()