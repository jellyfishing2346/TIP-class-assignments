#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'check_balanced' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#

def check_balanced(s):
    stack = []
    matching_parentheses = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in matching_parentheses.values():
            stack.append(char)
        elif char in matching_parentheses.keys():
            if not stack or stack[-1] != matching_parentheses[char]:
                return False
            stack.pop()
    return not stack
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    arr = ast.literal_eval(input_data)

    result = check_balanced(arr)
    print(result)