#!/usr/bin/env python3
"""
Constructs the tree shown in the question and prints a few representations.

Tree:
    10
   /  \
  5    15
 / \     \
2   7     20

This file demonstrates which code snippet creates that tree.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(20)
    return root


def level_order(root):
    from collections import deque
    if not root:
        return []
    q = deque([root])
    out = []
    while q:
        n = q.popleft()
        if n:
            out.append(n.val)
            q.append(n.left)
            q.append(n.right)
        else:
            out.append(None)
    # trim trailing Nones
    while out and out[-1] is None:
        out.pop()
    return out


def print_structure(root):
    print('Parent -> (left, right)')
    nodes = [(root, 'root')]
    seen = set()
    while nodes:
        node, name = nodes.pop(0)
        if node is None or id(node) in seen:
            continue
        seen.add(id(node))
        left = node.left.val if node.left else None
        right = node.right.val if node.right else None
        print(f"{node.val} -> ({left}, {right})")
        nodes.append((node.left, 'left'))
        nodes.append((node.right, 'right'))


if __name__ == '__main__':
    root = build_tree()
    print('Level-order list:', level_order(root))
    print()
    print_structure(root)
    print('\nAnswer: the option that performs exactly these assignments:')
    print("root = TreeNode(10); root.left = TreeNode(5); root.right = TreeNode(15); root.left.left = TreeNode(2); root.left.right = TreeNode(7); root.right.right = TreeNode(20)")
