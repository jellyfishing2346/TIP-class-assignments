#!/bin/python3

import math
import os
import random
import re
import sys
import ast
import json



def has_path(adjacency_dict, start, destination):
    # Fast path
    if start == destination:
        return True

    # We'll perform a DFS (stack) with a visited set.
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node == destination:
            return True
        if node in visited:
            continue
        visited.add(node)

        # Determine neighbors robustly. Expecting a dict mapping node->list,
        # but also tolerate an edge-list of pairs.
        neighbors = []
        if isinstance(adjacency_dict, dict):
            neighbors = adjacency_dict.get(node, []) or []
        else:
            # Try to interpret adjacency_dict as an iterable of edges
            try:
                for edge in adjacency_dict:
                    if isinstance(edge, (list, tuple)) and len(edge) >= 2:
                        if edge[0] == node:
                            neighbors.append(edge[1])
            except Exception:
                neighbors = []

        for n in neighbors:
            if n not in visited:
                stack.append(n)

    return False


if __name__ == '__main__':
    input_data = sys.stdin.read().strip()

    # Replace curly quotes with straight quotes
    input_data = input_data.replace('‘', "'").replace('’', "'")

    try:
        # Handle multiple test cases by splitting input on empty lines or multiple blocks
        input_blocks = input_data.splitlines()
        current_block = []

        # Process each line
        for line in input_blocks:
            stripped_line = line.strip()
            if stripped_line:
                # Collect non-empty lines into a block
                current_block.append(stripped_line)
            else:
                # When encountering an empty line, process the collected block
                if current_block:
                    input_string = ' '.join(current_block)
                    # Convert the collected block to a valid Python structure
                    test_case = ast.literal_eval(input_string)

                    # Extract the adjacency list, start, and destination
                    adjacency_dict = test_case[0]
                    start = test_case[1]
                    destination = test_case[2]
                    result = has_path(adjacency_dict, start, destination)
                    print(result)

                    # Reset for the next block
                    current_block = []

        # Process any remaining block after the loop
        if current_block:
            input_string = ' '.join(current_block)
            test_case = ast.literal_eval(input_string)
            adjacency_dict = test_case[0]
            start = test_case[1]
            destination = test_case[2]
            result = has_path(adjacency_dict, start, destination)
            print(result)

    except SyntaxError as e:
        print(f"SyntaxError in input: {e}")
    except Exception as e:
        # Print a simple error message to help debugging malformed inputs
        print(f"Error: {e}")
