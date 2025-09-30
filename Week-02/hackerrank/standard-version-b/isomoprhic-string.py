#!/bin/python

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'is_isomorphic' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#

def is_isomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_to_s = {}
    for a, b in zip(s, t):
        if (a in s_to_t and s_to_t[a] != b) or (b in t_to_s and t_to_s[b] != a):
            return False
        s_to_t[a] = b
        t_to_s[b] = a
    return True

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()

    for line in input_data:
        # Skip empty or improperly formatted lines
        if not line.strip():
            continue

        # Safely split the line
        try:
            s, t = line.split(",")
            s = s.strip().strip('"')
            t = t.strip().strip('"')
        except ValueError:
            print("Invalid input format:", line)
            continue

        result = is_isomorphic(s, t)
        outfile.write(str(result) + '\n')
    outfile.close()