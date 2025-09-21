#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'roman_to_integer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def roman_to_integer(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        value = roman[ch]
        if value < prev:
            total -= value
        else:
            total += value
        prev = value
    return total

if __name__ == "__main__":
    # Read all input
    input_data = sys.stdin.read().strip().split("\n")
    results = []

    for line in input_data:
        if not line.strip():  # If the input line is empty
            results.append(0)  # Return 0 for empty strings
            continue

        try:
            # Process Roman numeral string
            roman_string = line.strip()
            
            # Redirect debugging output to stderr
            original_stdout = sys.stdout
            try:
                sys.stdout = sys.stderr  # Redirect stdout to stderr for debugging prints
                result = roman_to_integer(roman_string)
            finally:
                sys.stdout = original_stdout  # Restore stdout

            # Append the result
            results.append(result)
        except KeyError:
            # Handle invalid Roman numeral input
            results.append("Invalid Roman numeral")

    # Print all results (one per line)
    for res in results:
        print(res)