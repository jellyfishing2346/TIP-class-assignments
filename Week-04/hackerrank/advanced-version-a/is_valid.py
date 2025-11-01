#!/bin/python

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

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0
if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()   

    for line in input_data:
        result = is_valid(line)
        outfile.write(str(result) + '\n')
    outfile.close()