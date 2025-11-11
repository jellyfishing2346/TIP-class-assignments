#!/usr/bin/env python3
"""
Example implementing find_max_depth for a binary tree and showing its time complexity.

This mirrors the recursive implementation shown in the screenshot and demonstrates
that the algorithm visits every node exactly once, so the time complexity is O(n).
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_max_depth(root):
    if not root:
        return 0
    left_depth = find_max_depth(root.left)
    right_depth = find_max_depth(root.right)
    return max(left_depth, right_depth) + 1


def build_sample_tree():
    # Build a small sample tree:
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    return n1


if __name__ == '__main__':
    root = build_sample_tree()
    depth = find_max_depth(root)
    print('Computed max depth:', depth)  # expect 3 for this tree
    print('Time complexity: O(n)')
