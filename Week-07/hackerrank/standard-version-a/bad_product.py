#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'next_greatest_letter' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY letters
#  2. STRING target
#

def next_greatest_letter(letters, target):
    # Write your code here
    all_letters = len(letters)
    low = 0
    high = all_letters - 1
    
    letter = letters[0]
    
    while low <= high:
        middle = (low + high) // 2
        
        if letters[middle] > target:
            letter = letters[middle]
            high = middle - 1
        else:
            low = middle + 1
    
    return letter
    


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        letters, target = eval(line)
        result = next_greatest_letter(letters, target)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()
