#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'find_kth_bit' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def find_kth_bit(n, k):
    invert = False
    # Loop to reduce the problem size (n) until we reach the base string S1
    while n > 1:
        # mid is the index of the middle '1' in S_n (1-indexed)
        mid = 1 << (n - 1)
        
        # Case 1: k is the middle bit (The '1' added in the Si construction)
        if k == mid:
            # The bit is '1', subject to the cumulative inversion parity
            return '0' if invert else '1'
        
        # Case 2: Left Half (1 <= k < mid)
        if k < mid:
            # The bit is the k-th bit of S_{n-1}. Reduce n.
            n -= 1
        
        # Case 3: Right Half (mid < k <= 2^n - 1)
        else:
            # The bit is in the reverse(invert(S_{n-1})) section.
            
            # 1. Map k to its mirrored position (j_orig) in S_{n-1}:
            #    j_orig = Length(S_n) - k + 1 = (2^n - 1) - k + 1 = 2^n - k
            k = (1 << n) - k
            
            # 2. The bit is INVERTED relative to the mirrored bit. Flip the overall parity.
            invert = not invert
            
            # 3. Reduce the problem size.
            n -= 1

    # Final Step: After the loop, n is 1, and k is 1. We are looking for the 1st bit of S1.
    # The original bit of S1 is '0'. The final result is this bit flipped by 'invert'.
    return '1' if invert else '0'


if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        n, k = eval(line)
        result = find_kth_bit(n, k)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()
