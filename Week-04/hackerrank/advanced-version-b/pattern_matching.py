#!/bin/python3

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'pattern_matching' function below.
#
# The function is expected to return a BOOLEAN_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY queries
#  2. STRING pattern
#

def pattern_matching(queries, pattern):
    # Write your code here
    def matches(query, pattern):
        i = 0  # Pointer for query
        j = 0  # Pointer for pattern
        
        while i < len(query):
            # Case 1: Match Found (Required by Pattern)
            if j < len(pattern) and query[i] == pattern[j]:
                i += 1
                j += 1
            
            # Case 2: Non-matching Uppercase in Query (Instant Failure)
            # If the query has an uppercase letter, it MUST match the pattern's 
            # current character (which is handled in Case 1). If we reach here 
            # and the query character is uppercase, it's an illegal extra character.
            elif query[i].isupper():
                return False
            
            # Case 3: Non-matching Lowercase in Query (Allowed Skip)
            # If the query character is lowercase and doesn't match the pattern,
            # we skip it in the query (advance i) and try to match the pattern's 
            # current character (j) against the next query character.
            else:
                i += 1

        # After the query is exhausted, the pattern must also be fully consumed 
        # (i.e., j must have reached the end of pattern).
        return j == len(pattern)

    # Main function logic: apply the 'matches' helper function to all queries
    results = []
    for query in queries:
        results.append(matches(query, pattern))
        
    return results

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        queries, pattern = eval(line)
        result = pattern_matching(queries, pattern)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()
