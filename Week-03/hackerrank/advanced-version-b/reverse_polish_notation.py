#!/bin/python

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'evalRPN' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY tokens as parameter.
#

def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in '+-*/':
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Truncate towards zero
    return stack[0]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        tokens = ast.literal_eval(line.strip())  
        result = evalRPN(tokens)
        outfile.write(str(result) + '\n')
    outfile.close()