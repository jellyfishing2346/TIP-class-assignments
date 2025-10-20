# Definition for a singly linked list node
class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

# The function to analyze
def mystery_function(head):
    # O(1) checks for empty or single-node list
    if not head or head.next:
        return None
    
    # O(n) traversal
    current = head
    while current.next and current.next.next:
        current = current.next
        
    # O(1) deletion and return
    current.next = None
    return head

# Time Complexity: O(n)
# Space Complexity: O(1)