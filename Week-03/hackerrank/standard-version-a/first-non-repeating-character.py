#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'first_non_repeating_character' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

from collections import deque

def first_non_repeating_character(s):
    from collections import Counter
    char_count = Counter(s)
    
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    
    return -1

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            s = ast.literal_eval(input_str)

            result = first_non_repeating_character(s)

            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")
    outfile.close()