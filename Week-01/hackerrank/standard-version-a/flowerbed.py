#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'can_place_flowers' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. INTEGER_ARRAY flowerbed
#  2. INTEGER n
#

def can_place_flowers(flowerbed, n):
    counting = 0
    flowerbed_length = len(flowerbed)
    for j in range(flowerbed_length):
        if flowerbed[j] == 0:
            left = (j == 0) or (flowerbed[j-1] == 0)
            right = (j == flowerbed_length - 1) or (flowerbed[j+1] == 0)
            if left and right:
                flowerbed[j] = 1
                counting += 1
                if counting > n:
                    return True
    return counting >= n


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    
    results = []
    for i in range(0, len(input_data), 2):
        flowerbed_line = input_data[i].strip()
        n = int(input_data[i + 1].strip())
        
        if flowerbed_line == "[]":
            flowerbed = []
        else:
            flowerbed = list(map(int, flowerbed_line.strip("[]").split(",")))

        # Redirect debugging output to stderr
        original_stdout = sys.stdout
        try:
            sys.stdout = sys.stderr
            result = can_place_flowers(flowerbed, n)
        finally:
            sys.stdout = original_stdout

        results.append(result)
    
    for res in results:
        print(res)