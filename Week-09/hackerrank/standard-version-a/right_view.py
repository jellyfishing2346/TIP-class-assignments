#!/bin/python3

import os
import sys
import ast
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def right_view(root):
    # Return the list of node values visible from the right side
    if not root:
        return []
    view = []
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            # if it's the last node in this level, include it
            if i == level_size - 1:
                view.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return view


def list_to_tree(lst):
    if not lst:
        return None
    # treat Python None as missing
    if lst[0] is None:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while i < len(lst):
        node = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == '__main__':
    outfile = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
    input_data = sys.stdin.read().strip()
    if not input_data:
        outfile.write(str([]) + '\n')
        outfile.close()
        sys.exit(0)

    lines = input_data.splitlines()
    for data in lines:
        if data.strip() == '':
            continue
        data = data.replace('null', 'None')
        arr = ast.literal_eval(data)
        root = list_to_tree(arr)
        res = right_view(root)
        outfile.write(str(res) + '\n')
    outfile.close()
