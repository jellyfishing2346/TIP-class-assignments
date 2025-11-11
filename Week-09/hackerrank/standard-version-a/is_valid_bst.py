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



def is_valid_bst(root):
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        
        if node.val < low or node.val > high: 
            return False
        
        return (validate(node.left, low, node.val) and
                validate(node.right, node.val, high))
    
    return validate(root)

def build_tree(nodes):
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = [root]
    index = 1
    
    while queue and index < len(nodes):
        node = queue.pop(0)
        
        if nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1
        
        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1
    
    return root


if __name__ == '__main__':
    input_data = sys.stdin.read().strip()

    input_data = input_data.replace('null', 'None')

    nodes = ast.literal_eval(input_data)
    root = build_tree(nodes)
    
    result = is_valid_bst(root)
    print(result)