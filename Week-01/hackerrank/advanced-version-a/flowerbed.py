#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'can_place_flowers' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY flowerbed
#  2. INTEGER n
#

def can_place_flowers(flowerbed, n):
    flowerbed = flowerbed[:]
    counting = 0
    j = 0
    flowerbed_length = len(flowerbed)
    while j < flowerbed_length:
        if flowerbed[j] == 0:
            left = (j == 0) or (flowerbed[j - 1] == 0)
            right = (j == flowerbed_length - 1) or (flowerbed[j + 1] == 0)
            if left and right:
                flowerbed[j] = 1
                counting += 1
                if counting >= n:
                    return True
                j += 2
                continue
        j += 1
    return counting >= n

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    for line in input_data:
        match = re.match(r"(\[.*\]),\s*(\d+)", line)
        if match:
            flowerbed_str = match.group(1)
            n_str = match.group(2)
            
            flowerbed = ast.literal_eval(flowerbed_str)
            n = int(n_str)
            result = can_place_flowers(flowerbed, n)
            outfile.write(str(result) + '\n')
    outfile.close()