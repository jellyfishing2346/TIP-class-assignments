#!/bin/python3

import math
import os
import random
import re
import sys
import ast

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left = left
        self.right = right

def root_equals_sum_of_descendants(root):
    # Return True if root.val equals the sum of all values in its descendants
    if not root:
        return False

    # Compute total sum of all nodes iteratively to avoid recursion depth issues.
    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node is None:
            continue
        total += node.val
        stack.append(node.left)
        stack.append(node.right)

    # Sum of descendants = total - root.val
    return root.val * 2 == total

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root
    
if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()   
    
    for data in input_data:
       
        root_list = ast.literal_eval(data)
        root = list_to_tree(root_list)
        
        result = root_equals_sum_of_descendants(root)

        outfile.write(str(result) + '\n')
    outfile.close()