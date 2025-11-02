class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

def mystery_function(head_a, head_b):
    if head_a is None or head_b is None:
        return head_a, head_b
    head_a.next, head_b.next = head_b.next, head_a.next
    return head_a, head_b
# Input Lists:
head_a = Node(1, Node(2, Node(3)))
head_b = Node(4, Node(5, Node(6)))
new_head_a, new_head_b = mystery_function(head_a, head_b)
# Output Lists:
# new_head_a: 4 -> 2 -> 3
# new_head_b: 1 -> 5 -> 6