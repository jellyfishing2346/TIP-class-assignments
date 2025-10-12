#!/bin/python

import math
import os
import random
import re
import sys
import ast
import json



#
# Complete the 'is_valid_sudoku' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING_ARRAY board as parameter.
#

def is_valid_sudoku(board):
    # Write your code here
    seen = set()
    
    for r in range(9):
        for c in range(9):
            val = board[r][c]
            
            # Skip empty cells
            if val != '.':
                
                # Create three unique identifiers for this cell's value:
                # 1. Row Constraint: (0, row_index, value)
                row_key = (0, r, val)
                
                # 2. Column Constraint: (1, col_index, value)
                col_key = (1, c, val)
                
                # 3. 3x3 Box Constraint: (2, box_row_index, box_col_index, value)
                # The box coordinates are (r // 3, c // 3)
                box_key = (2, r // 3, c // 3, val)
                
                # Check for duplication: if any key is already 'seen', the board is invalid.
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                # If valid so far, add all three keys to the set
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
                
    return True

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip()
    
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
                    board = test_case[0]
                    result = is_valid_sudoku(board)
                    outfile.write(str(result) + '\n')

                    # Reset for the next block
                    current_block = []

        # Process any remaining block after the loop
        if current_block:
            input_string = ' '.join(current_block)
            test_case = ast.literal_eval(input_string)
            board = test_case[0]
            result = is_valid_sudoku(board)
            outfile.write(str(result) + '\n')

    except SyntaxError as e:
        print(f"SyntaxError in input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    outfile.close()
