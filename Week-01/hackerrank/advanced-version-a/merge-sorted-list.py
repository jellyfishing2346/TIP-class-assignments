#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'merge_sorted_lists' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY lst1
#  2. INTEGER_ARRAY lst2
#

def merge_sorted_lists(lst1, lst2):
    i, j = 0, 0
    merged = []
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    merged.extend(lst1[i:])
    merged.extend(lst2[j:])
    return merged

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip()
    
    input_lines = input_data.splitlines()
    
    for line in input_lines:
        lists = re.split(r'\s*,\s*(?=\[)', line)
        
        if len(lists) != 2:
            raise ValueError("Input format is incorrect. Expected two lists separated by a comma.")
    
        lst1 = ast.literal_eval(lists[0].strip())
        lst2 = ast.literal_eval(lists[1].strip())
        
        # Merge the lists
        result = merge_sorted_lists(lst1, lst2)
        
        # Print the result
        outfile.write(str(result) + '\n')
    outfile.close()