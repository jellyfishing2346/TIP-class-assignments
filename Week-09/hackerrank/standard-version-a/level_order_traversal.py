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



def level_order_traversal(root):
    # Return level-order traversal as a list of levels (list of lists)
    if not root:
        return []
    levels = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        levels.append(level)
    return levels

def build_tree(nodes):
    if not nodes:
        return None

    # If the first element is None (e.g. input '[null]'), there is no tree
    if nodes[0] is None:
        return None

    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1

    while queue and i < len(nodes):
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
        
        root = build_tree(tree_list)
        result = level_order_traversal(root)
        outfile.write(str(result) + '\n')
    outfile.close()