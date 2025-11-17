#!/bin/python3

import math
import os
import random
import re
import sys
import ast



def dfs(matrix, start):
    if not matrix:
        return []
    n = len(matrix)
    # ensure matrix is at least n x n
    if any(len(row) != n for row in matrix):
        raise ValueError("Adjacency matrix must be square (n x n).")
    if not (0 <= start < n):
        raise IndexError("start index out of range")

    visited = set()
    result = []

    def dfs_recursive(node):
        if node in visited:
            return
        visited.add(node)
        result.append(node)

        for neighbor in range(n):
            if matrix[node][neighbor]:  # truthy check; use ==1 if you require exact values
                if neighbor not in visited:          # optional, minor optimization
                    dfs_recursive(neighbor)

    dfs_recursive(start)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_data = sys.stdin.read().strip()
    dict_strings = input_data.split("\n\n")
    
    for dict_string in dict_strings:
        input_list = ast.literal_eval(dict_string.strip())
        matrix = input_list[0]
        start = input_list[1]
        result = dfs(matrix, start)
        fptr.write(str(result) + '\n')

    fptr.close()