#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_nested' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING paren_s as parameter.
#

def is_nested_parens(paren_s):
    # Accept only parentheses characters. Return True if they form a
    # properly balanced/nested sequence, False otherwise.
    if paren_s is None:
        return False

    # Ensure input is a string
    try:
        s = str(paren_s)
    except Exception:
        return False

    # Empty string is considered nested (no parentheses)
    if s == "":
        return True

    depth = 0
    for ch in s:
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
            if depth < 0:
                return False
        else:
            # Any other character makes the string invalid for this check
            return False

    return depth == 0


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        paren_s = ast.literal_eval(line.strip()) 
        result = is_nested_parens(paren_s)
        outfile.write(str(result) + '\n')
    outfile.close()
