class ListNode:
    def __init__(self, val, data=None):
        self.val = val
        self.next = next
def insert_at_head(head, val): 
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# Time Complexity: O(1)
# Space Complexity: O(1)