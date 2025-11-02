#!/usr/bin/env python3
"""
Builds the small tree from the screenshot and prints two representations:
 - an indented preorder print (visual hierarchy)
 - a level-order list (breadth-first order)

Tree structure being created:
    a
   / \
  x   y
 / \   \
e   m   p

"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    a = TreeNode('a')
    x = TreeNode('x')
    y = TreeNode('y')
    e = TreeNode('e')
    m = TreeNode('m')
    p = TreeNode('p')

    a.left = x
    a.right = y
    x.left = e
    x.right = m
    y.right = p

    root = a
    return root


def print_preorder(node, indent=0):
    if node is None:
        return
    print(' ' * indent + str(node.val))
    print_preorder(node.left, indent + 4)
    print_preorder(node.right, indent + 4)


def level_order_list(root):
    from collections import deque
    if root is None:
        return []
    q = deque([root])
    out = []
    while q:
        n = q.popleft()
        out.append(n.val)
        if n.left:
            q.append(n.left)
        if n.right:
            q.append(n.right)
    return out


if __name__ == '__main__':
    root = build_tree()
    print('Indented preorder representation:')
    print_preorder(root)
    print()
    print('Level-order (breadth-first) list:', level_order_list(root))