class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mystery_function(head, val):
    index = 0
    current = head
    
    # Loop continues as long as 'current' node is not None
    while current:
        # Check if the current node's value matches the target value 'val'
        if current.val == val:
            # If found, immediately return the current index
            return index
        
        # Move to the next node in the list
        current = current.next
        
        # Increment the index for the next node
        index += 1
        
    # If the loop finishes without finding the value, return -1
    return -1

# --- Setup ---
# Create Linked List: 10 -> 20 -> 30
head = ListNode(10)
head.next = ListNode(20)
head.next.next = ListNode(30)

# The function call:
print(mystery_function(head, 10))
