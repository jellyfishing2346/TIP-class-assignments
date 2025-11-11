#!/usr/bin/env python3
"""
Implements the mystery function from the screenshot and runs the sample tree.

Expected output for the pictured tree: "right" (right subtree has more nodes).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_nodes(node):
    if not node:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)


def mystery_function(root):
    if not root:
        return "empty"
    left_count = count_nodes(root.left)
    right_count = count_nodes(root.right)
    if left_count > right_count:
        return "left"
    elif right_count > left_count:
        return "right"
    else:
        return "equal"


def build_sample_tree():
    # Build the tree from the screenshot
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(4)
    # root.right = TreeNode(3)
    # root.right.left = TreeNode(5)
    # root.right.right = TreeNode(6)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


if __name__ == '__main__':
    root = build_sample_tree()
    result = mystery_function(root)
    print(result)
