#!/bin/python

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'longest_palindrome' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def longest_palindrome(s):
    import collections
    
    ch_counts = collections.Counter(s)
    
    total = 0
    isOdd = False
    
    for ch in ch_counts.values():
        total += (ch // 2) * 2
        if ch % 2 == 1:
            isOdd = True
    
    if isOdd:
        total += 1
        
    return total 

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        s = ast.literal_eval(line.strip())   
        result = longest_palindrome(s)
        outfile.write(str(result) + '\n')
    outfile.close()