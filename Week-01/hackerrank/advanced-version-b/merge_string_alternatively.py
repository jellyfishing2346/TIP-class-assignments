#!/bin/python

import math
import os
import random
import re
import sys
import ast



# Complete the 'merge_alternately' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING word1
#  2. STRING word2
#

def merge_alternately(word1, word2):
    # Write your code here
    merged = []
    i, j = 0, 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            merged.append(word1[i])
            i += 1
        if j < len(word2):
            merged.append(word2[j])
            j += 1
    return ''.join(merged)

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_lines = sys.stdin.read().strip().splitlines()
    
    for input_str in input_lines:
        if input_str.strip() == "":  
            continue
        
        try:
            # Split the input based on a comma to get the two words
            word1, word2 = input_str.split(',')
            word1 = word1.strip()
            word2 = word2.strip()
            
            result = merge_alternately(word1, word2)

            outfile.write(str(result) + '\n')
        except ValueError:
            print("Error: Invalid input")
    outfile.close()