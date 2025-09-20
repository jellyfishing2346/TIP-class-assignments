#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'first_repeating_substring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
from collections import defaultdict

def first_repeating_substring(s, k):
    # Write your code here
    counting = defaultdict(int)
    for j in range(len(s) - k + 1):
        string = s[j:j + k]
        counting[string] += 1
    for m in range(len(s) - k + 1):
        string = s[m:m + k]
        if counting[string] == 2:
            return m
    return -1

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_str = sys.stdin.read().strip().splitlines()
    
    for line in input_str:
        s, k = line.split(', ')
        s = s.strip('"')
        k = int(k)
        result = first_repeating_substring(s, k)
        outfile.write(str(result) + '\n')
    outfile.close()