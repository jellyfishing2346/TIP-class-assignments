class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def mystery_function(head):
    if head is None:
        return None

    if head.next is None:
        return None

    current = head
    while current.next.next is not None:
        current = current.next
        
    current.next = None
    return head

# Input List: 1 -> 2 -> 3
# head = Node(1, Node(2, Node(3))) 
# new_head = mystery_function(head)
# Output List: 1 -> 2