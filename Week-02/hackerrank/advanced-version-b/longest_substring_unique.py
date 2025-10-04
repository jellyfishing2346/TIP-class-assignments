#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'length_of_longest_substring' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def length_of_longest_substring(s):
    char_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character is already in current window, move left pointer
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        
        # Update the character's position
        char_map[s[right]] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        s = line.strip().strip('"')  
        result = length_of_longest_substring(s)
        outfile.write(str(result) + '\n')
    outfile.close()
