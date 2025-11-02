#!/bin/python3

import math
import os
import random
import re
import sys
import ast
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delete_node(root, key):
    # Write your code here
    if root is None:
        return None
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = delete_node(root.right, successor.val)
    return root

def build_tree_from_list(lst):
    if not lst:
        return None

    nodes = [TreeNode(val) if val is not None else None for val in lst]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    
    return root

def tree_to_list(root):
    if not root:
        return []
    
    result, queue = [], [root]
    while any(queue):
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
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
       
        root = build_tree_from_list(tree_list)
        result = delete_node(root, val)
        
        print(tree_to_list(result))