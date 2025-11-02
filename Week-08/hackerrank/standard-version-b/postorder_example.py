#!/usr/bin/env python3
"""
Builds the example binary tree and prints its postorder traversal.

Tree used (from screenshot):
    1
   / \
  2   3
 / \
4   5

Postorder should be: [4, 5, 2, 3, 1]
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree():
    # nodes
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)

    # links
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5

    return n1


def postorder(root):
    res = []

    def dfs(node):
        if node is None:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res


if __name__ == '__main__':
    root = build_tree()
    trav = postorder(root)
    print(trav)
