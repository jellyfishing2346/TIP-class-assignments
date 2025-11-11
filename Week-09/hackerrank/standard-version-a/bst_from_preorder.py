#!/bin/python3

import os
import sys
import ast

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert_node(root, val):
    if val < root.val:
        if root.left:
            insert_node(root.left, val)
        else:
            root.left = TreeNode(val)
    else:
        if root.right:
            insert_node(root.right, val)
        else:
            root.right = TreeNode(val)


def bst_from_preorder(preorder):
    # Build BST by inserting nodes in preorder order
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    for v in preorder[1:]:
        insert_node(root, v)
    return root


def print_tree(root):
    """ Helper function to print the tree nodes in level order. """
    if not root:
        return []
    queue = [root]
    result = []
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append("None")
    # Remove trailing "None" values that represent missing nodes at the end of the tree
    while result and result[-1] == "None":
        result.pop()
    return result


if __name__ == '__main__':
    outfile = open(os.environ.get('OUTPUT_PATH', '/dev/stdout'), 'w')
    input_data = sys.stdin.read().strip()

    input_data = input_data.splitlines()

    for data in input_data:
        if data.strip() == "":
            continue

        preorder = ast.literal_eval(data)

        root = bst_from_preorder(preorder)
        result = print_tree(root)
        outfile.write(str(result) + '\n')
    outfile.close()
