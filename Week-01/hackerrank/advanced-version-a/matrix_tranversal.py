#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'get_sum_of_odds' function below.
#
# The function is expected to return an INTEGER_ARRAY.
#

def get_sum_of_odds(matrix):
    odds = [num for row in matrix for num in row if num % 2 == 1]
    return [len(odds), sum(odds)]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = input()
    while (input_data != "END"):
        matrix = ast.literal_eval(input_data)

        result = get_sum_of_odds(matrix)
        outfile.write(str(result) + '\n')
        input_data = input()
    outfile.close()