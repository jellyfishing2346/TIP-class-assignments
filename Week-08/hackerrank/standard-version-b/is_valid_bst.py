#/python3

import math
import os
import random
import re
import sys
import ast

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Helper function to create a tree from a list (level-order traversal)
def create_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root



# Complete the `is_valid_bst` function below
def is_valid_bst(root):
    def validate(node, low, high):
        if not node:
            return True
        if node.val <= low or node.val >= high:
            return False
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))

    return validate(root, float('-inf'), float('inf'))
if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().strip().split("\n")
    results = []

    for line in input_data:
        values = eval(line)  # Parse the input as a list
        root = create_tree(values)
        results.append(is_valid_bst(root))

    for res in results:
        print(res)