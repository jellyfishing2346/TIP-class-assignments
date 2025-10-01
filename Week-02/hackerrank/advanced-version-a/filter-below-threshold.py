#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'filter_below_threshold' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY dict1
#  2. INTEGER threshold
#

def filter_below_threshold(dict1, threshold):
    filtered_dict = {}
    for key, value in dict1.items():
        if value > threshold:  # Only keep values strictly more than threshold
            filtered_dict[key] = value
    return filtered_dict

if __name__ == '__main__':
    import sys
    import ast
    import io

    # Capture original stdout
    original_stdout = sys.stdout  
    sys.stdout = io.StringIO()  # Redirect stdout to a temporary buffer

    try:
        input_data = sys.stdin.read().strip()
        input_list = ast.literal_eval(input_data)

        dict1 = input_list[0]
        threshold = input_list[1]

        result = filter_below_threshold(dict1, threshold)

    finally:
        sys.stdout = original_stdout  # Restore original stdout

    print(result)  # This is the ONLY output the system reads