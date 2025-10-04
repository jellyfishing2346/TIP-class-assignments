#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_palindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING s as parameter.
#

def is_palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from left
        while left < right and not s[left].isalnum():
            left += 1
        
        # Skip non-alphanumeric characters from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower(): 
            return False
        
        left += 1
        right -= 1

    return True
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    arr = ast.literal_eval(input_data)

    result = is_palindrome(arr)
    print(result)
