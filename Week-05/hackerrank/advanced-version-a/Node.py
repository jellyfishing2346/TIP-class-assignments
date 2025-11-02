class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node

def mystery_function(head):
    # Case 1: Empty list
    if head is None:
        return None

    # Case 2: List with only one node (head.next is None)
    if head.next is None:
        return head

    # Initialization
    current = head
    
    # Loop: Traverses the list until current.next.next is None
    # current.next.next is the node AFTER the next node.
    while current.next.next: 
        # Moves 'current' one step forward
        current = current.next

    # Loop Termination Condition:
    # The loop stops when 'current' is the second-to-last node.
    # At this point, current -> current.next -> None.
    # The list is still intact.

    # Return Value:
    # The function returns the node that the loop stopped at, which is the 
    # second-to-last node of the original list.
    return current

# --- Input List Setup ---
# Input List: 1 -> 2 -> 3
# The image shows a shorthand, but we must construct the list properly.

# Assuming a proper list construction helper/constructor for the Doubly Linked List:
# head = Node(1, Node(2, Node(3))) 
# We ignore 'prev' for simplicity of this unidirectional traversal, but acknowledge the class structure.
node3 = Node(3)
node2 = Node(2, next_node=node3)
node3.prev = node2 # (If we were being fully accurate)
head = Node(1, next_node=node2)
node2.prev = head # (If we were being fully accurate)

# Output: 2 -> 3 -> None