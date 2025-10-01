#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'grouped' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY strs as parameter.
#

def grouped_anagrams(strs):
    from collections import defaultdict
    groups = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        groups[key].append(word)
    return list(groups.values())

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            strs = ast.literal_eval(input_str)

            result = grouped_anagrams(strs)

            result = [sorted(group) for group in result]
            result = sorted(result, key=lambda x: x[0] if x else '')

            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")
    outfile.close()