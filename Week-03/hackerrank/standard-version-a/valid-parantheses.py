#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_valid' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#

def is_valid(s):
    stack = []
    open_and_close = {'(': ')', '{': '}', '[': ']'}
    for ch in s:
        if ch in open_and_close:  # Opening bracket
            stack.append(ch)
        else:  # Closing bracket
            if not stack or open_and_close[stack.pop()] != ch:
                return False
    return not stack

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            s = ast.literal_eval(input_str)

            result = is_valid(s)

            outfile.write(str(result) + '\n')
        except (ValueError, SyntaxError):
            print("Error: Invalid input")
    outfile.close()