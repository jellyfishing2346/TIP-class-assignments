#!/bin/python

import math
import os
import random
import re
import sys
import ast



def is_palindrome(s):
    left, right = 0, len(s) - 1 

    while left < right:
        if not s[left].isalnum():
            left += 1  
        elif not s[right].isalnum():
            right -= 1  
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    
    return True

if __name__ == '__main__':
    nput_data = sys.stdin.read().strip()
    arr = ast.literal_eval(input_data)

    result = is_palindrome(arr)
    print(result)