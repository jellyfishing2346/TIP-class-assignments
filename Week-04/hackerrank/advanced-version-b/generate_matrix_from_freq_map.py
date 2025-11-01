#!/bin/python

import math
import os
import random
import re
import sys
import ast


#
# Complete the 'generate_matrix_from_freq_map' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY freq_map as parameter.
#

def generate_matrix_from_freq_map(freq_map):
    # Write your code here
    # Accept either a list/tuple of values or a dict mapping (e.g., prime->count).
    # If freq_map is a dict, convert to list of values ordered by numeric keys.
    if freq_map is None:
        return []

    # Turn into a list of values
    if isinstance(freq_map, dict):
        try:
            # sort keys numerically when possible
            items = sorted(freq_map.items(), key=lambda kv: int(kv[0]))
            values = [v for k, v in items]
        except Exception:
            # fallback: preserve insertion order of dict values
            values = list(freq_map.values())
    else:
        # try to coerce to list (supports lists, tuples, etc.)
        try:
            values = list(freq_map)
        except Exception:
            # not iterable -> return empty
            return []

    matrix = []
    for i in range(0, len(values), 3):
        row = values[i:i+3]
        matrix.append(row)
    return matrix

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()  
    
    for line in input_data:
        if line.strip():   
            try:
                freq_map = ast.literal_eval(line)
                result = generate_matrix_from_freq_map(freq_map)
                outfile.write(str(result) + '\n')
            except (ValueError, SyntaxError) as e:
                print(f"Error processing line: {line}. Error: {e}")
    outfile.close()