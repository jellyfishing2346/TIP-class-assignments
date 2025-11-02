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


def is_symmetric(root):
    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.val == t2.val and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    return is_mirror(root, root)

def list_to_tree(lst):
    if not lst:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1

    while i < len(lst):
        node = queue.popleft()

        # Handle the left child
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        else:
            node.left = None
        i += 1

        # Handle the right child
        if i < len(lst):
            if lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
            else:
                node.right = None
            i += 1

    return root

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_data)

    root = list_to_tree(input_list)

    result = is_symmetric(root)
    print(result)