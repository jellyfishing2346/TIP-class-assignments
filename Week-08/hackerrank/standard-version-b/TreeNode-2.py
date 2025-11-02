class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode('a')
b = TreeNode('b')
c = TreeNode('c')
d = TreeNode('d')
e = TreeNode('e')

a.left = b
a.right = c
b.left = d
b.right = e

root = a

print("Root value:", root.val)  # Output: a
print("Left child of root:", root.left.val)  # Output: b
print("Right child of root:", root.right.val)  # Output: c
print("Left child of b:", root.left.left.val)  # Output: d
print("Right child of b:", root.left.right.val)  # Output: e
