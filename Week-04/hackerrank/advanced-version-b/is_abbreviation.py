#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_valid_abbreviation' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING abbr
#

def is_valid_abbreviation(s, abbr):
    # Write your code here
    """
    Checks if a string 'abbr' is a valid abbreviation of the string 's'.
    Numbers in 'abbr' represent a count of skipped characters in 's'.
    """
    s_ptr = 0    # Pointer for the full word s
    abbr_ptr = 0 # Pointer for the abbreviation abbr

    while abbr_ptr < len(abbr):
        # Case 1: Character match
        if abbr[abbr_ptr].isalpha():
            # Check if the word pointer has run out or if the characters don't match
            if s_ptr >= len(s) or s[s_ptr] != abbr[abbr_ptr]:
                return False
            
            # Match found, advance both pointers
            s_ptr += 1
            abbr_ptr += 1
        
        # Case 2: Numeric skip
        elif abbr[abbr_ptr].isdigit():
            # A number cannot start with a zero (e.g., "a02e" is invalid)
            if abbr[abbr_ptr] == '0':
                return False
            
            # Read the full multi-digit number
            num_str = ""
            while abbr_ptr < len(abbr) and abbr[abbr_ptr].isdigit():
                num_str += abbr[abbr_ptr]
                abbr_ptr += 1
            
            num_skip = int(num_str)
            
            # Advance the word pointer by the skip amount
            s_ptr += num_skip
            
        else:
            # Handle invalid characters in abbr (e.g., symbols)
            return False

    # After iterating through all of 'abbr', the word pointer 's_ptr' must be 
    # exactly at the end of the word 's' for a valid match.
    return s_ptr == len(s)

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        s, abbr = eval(line)
        result = is_valid_abbreviation(s, abbr)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()
