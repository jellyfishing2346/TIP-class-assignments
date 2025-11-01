#!/bin/python3

import math
import os
import random
import re
import sys
import ast


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
#
# Complete the 'prime_frequency_map' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY matrix as parameter.
#

def prime_frequency_map(matrix):
    # Write your code here
    prime_count = {}
    for row in matrix:
        for num in row:
            if is_prime(num):
                if num in prime_count:
                    prime_count[num] += 1
                else:
                    prime_count[num] = 1
    result = []
    for prime in sorted(prime_count.keys()):
        result.append(prime_count[prime])
    return result

if __name__ == '__main__':
    # Read input (HackerRank provides a Python literal for the matrix on stdin)
    input_data = sys.stdin.read().strip()
    if not input_data:
        matrix = []
    else:
        matrix = None
        # 1) Try Python literal (e.g., HackerRank sometimes provides a Python list literal)
        try:
            matrix = ast.literal_eval(input_data)
        except Exception:
            matrix = None

        # 2) Try JSON array
        if matrix is None:
            try:
                import json

                matrix = json.loads(input_data)
            except Exception:
                matrix = None

        # 3) Fallback: parse as whitespace-separated matrix. Support optional first line with dimensions.
        if matrix is None:
            lines = [l for l in input_data.splitlines() if l.strip()]
            matrix = []
            if not lines:
                matrix = []
            else:
                # If first line contains two integers, treat them as rows and cols
                first_nums = re.findall(r'-?\d+', lines[0])
                if len(first_nums) >= 2 and len(lines) > 1:
                    try:
                        r, c = int(first_nums[0]), int(first_nums[1])
                        # collect all ints from remaining lines
                        all_nums = []
                        for ln in lines[1:]:
                            all_nums.extend([int(x) for x in re.findall(r'-?\d+', ln)])
                        # reshape into r rows of length c if possible
                        if r * c <= len(all_nums):
                            matrix = [all_nums[i * c:(i + 1) * c] for i in range(r)]
                        else:
                            # not enough numbers: try to parse each line as a row
                            matrix = []
                            for ln in lines[1:]:
                                row = [int(x) for x in re.findall(r'-?\d+', ln)]
                                if row:
                                    matrix.append(row)
                    except Exception:
                        # fallback to parse each line as ints
                        matrix = []
                        for ln in lines:
                            row = [int(x) for x in re.findall(r'-?\d+', ln)]
                            if row:
                                matrix.append(row)
                else:
                    # Parse each non-empty line into a list of ints
                    for ln in lines:
                        row = [int(x) for x in re.findall(r'-?\d+', ln)]
                        if row:
                            matrix.append(row)

    result = prime_frequency_map(matrix)
    out_str = str(result) + "\n"

    output_path = os.environ.get('OUTPUT_PATH')
    if output_path:
        with open(output_path, 'w') as outfile:
            outfile.write(out_str)
    else:
        # When OUTPUT_PATH isn't provided (local runs), write to stdout for convenience
        sys.stdout.write(out_str)