class TreeNode:
    def __init__(self, val=0, left_child=None, right_child=None):
        self.val = val
        self.left = left_child
        self.right = right_child
def mystery_function(node):
    if not node:
        return 0
    left_result = mystery_function(node.left_child)
    right_result = mystery_function(node.right_child)
    return max(left_result, right_result) + node.val

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree