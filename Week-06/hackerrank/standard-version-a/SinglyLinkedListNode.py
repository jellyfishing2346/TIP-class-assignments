class SinglyLinkedListNode:
    def __init__(self, node_data, next_node=None):
        self.data = node_data
        self.next = next_node

def mystery_function(head):
    # Base Case: Empty list or single-node list
    if not head or not head.next:
        return head
    
    # Traverse to find the tail (last node) and prev (second-to-last node)
    prev = None
    tail = head
    while tail.next:
        prev = tail
        tail = tail.next
    
    # This condition should only be true for a single-node list, 
    # which is already handled by the base case, but kept for robustness.
    if not prev:
        return head
        
    # Re-linking steps:
    # 1. Set the tail's next to the second node (head.next)
    tail.next = head.next
    
    # 2. Set the second-to-last node's next to the head (to connect the tail)
    prev.next = head
    
    # 3. Disconnect the head from the second node (head becomes the new tail)
    head.next = None
    
    # Return the original tail, which is now the new head of the list
    return tail

# Example Input List: 1 -> 2 -> 3 -> 4 -> 5
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# new_head = mystery_function(head)

head = SinglyLinkedListNode(1, SinglyLinkedListNode(2, SinglyLinkedListNode(3, SinglyLinkedListNode(4, SinglyLinkedListNode(5)))))

new_head = mystery_function(head)
print(new_head.data)  # Output should be 5
print(new_head.next.data)  # Output should be 2
print(new_head.next.next.data)  # Output should be 3
print(new_head.next.next.next.data)  # Output should be 4
print(new_head.next.next.next.next.data)  # Output should be 1  # Output should be None
print(new_head.next.next.next.next.next)  # Output should be None