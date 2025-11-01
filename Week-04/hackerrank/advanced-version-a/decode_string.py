#!/bin/python

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'decode_string' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decode_string(s):
    # Stack to hold repetition counts (integers)
    num_stack = []
    # Stack to hold partially built strings before a bracket is closed
    str_stack = []
    
    current_num = 0
    current_string = ""
    
    for char in s:
        if char.isdigit():
            # Build the repetition number (handles multi-digit numbers like '10')
            current_num = current_num * 10 + int(char)
        
        elif char == '[':
            # Push the current string fragment and the current number onto their respective stacks
            str_stack.append(current_string)
            num_stack.append(current_num)
            
            # Reset current variables for the new nested scope
            current_string = ""
            current_num = 0
            
        elif char == ']':
            # Pop the previous repetition count and the previous string fragment
            num = num_stack.pop()
            prev_string = str_stack.pop()
            
            # Repeat the current_string 'num' times and prepend the prev_string
            current_string = prev_string + current_string * num
            
        else:
            # Must be a letter; append it to the current string fragment
            current_string += char
            
    return current_string

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        arr = ast.literal_eval(line.strip())   
        result = decode_string(arr)
        outfile.write(str(result) + '\n')
    outfile.close()

