#!/bin/python3

import math
import os
import random
import re
import sys
import ast



# Enter your code here. Read input from STDIN. Print output to STDOUT
#
# Complete the 'roman_to_int' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def roman_to_int(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    
    for char in reversed(s):
        value = roman[char]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    
    return total

if __name__ == '__main__':    
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        s = line.strip().strip('"')  
        result = roman_to_int(s)
        outfile.write(str(result) + '\n')
    outfile.close()
