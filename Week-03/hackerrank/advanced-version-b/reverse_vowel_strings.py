#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'reverse_vowels' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    s_list = list(s)
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1
        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1
    return ''.join(s_list)


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().split('\n')
    
    for line in input_data:
        s = line.strip().strip('"')  
        result = reverse_vowels(s)
        outfile.write(str(result) + '\n')
    outfile.close()

