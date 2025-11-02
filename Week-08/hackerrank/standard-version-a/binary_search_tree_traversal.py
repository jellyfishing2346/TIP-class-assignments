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
        self.left = left
        self.right = right



def insert_into_bst(root, val):
    # Write your code here
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    for val in values[1:]:
        insert_into_bst(root, val)
    return root

def bst_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing 'None' values
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == '__main__':
    input_data = sys.stdin.read().strip().splitlines()
    
    for data in input_data:
        tree_data, val = data.split('],')
        tree_data += ']'  
        val = int(val.strip())   
        
        tree_list = ast.literal_eval(tree_data)   
       
        root = build_tree(tree_list)
        result = insert_into_bst(root, val)
        
        print(bst_to_list(result))