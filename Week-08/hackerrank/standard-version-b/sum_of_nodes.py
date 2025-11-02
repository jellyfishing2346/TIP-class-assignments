#!/bin/python3

import math
import os
import random
import re
import sys
import ast

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sum_of_nodes(root):
    # Write your code here
    if root is None:
        return 0
    return root.val + sum_of_nodes(root.left) + sum_of_nodes(root.right)

def list_to_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while i < len(nodes):
        current = queue.popleft()
        
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    
    return root

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip()

    input_data = input_data.splitlines()
    
    for data in input_data:
        if data.strip() == "":
            continue   
        
        data = data.replace('null', 'None')
        tree_list = ast.literal_eval(data)
        
        root = list_to_tree(tree_list)
        result = sum_of_nodes(root)
        outfile.write(str(result) + '\n')
    outfile.close()