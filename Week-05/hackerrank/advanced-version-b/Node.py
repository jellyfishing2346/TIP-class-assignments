class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
def mystery_function(head_a, head_b):
    if head_a is None or head_b is None:
        return head_b, head_a
    head_a.next, head_b.next = head_a.next, head_b.next
    return head_b, head_a

# Input Lists
# List 1: 1 -> 2 -> 3 -> None
head_a = Node(1, Node(2, Node(3)))
# List 2: 4 -> 5 -> 6 -> None
head_b = Node(4, Node(5, Node(6)))
head_a, head_b = mystery_function(head_a, head_b)
print(head_a.value)  # Output: 4
print(head_a.next.value)  # Output: 2
print(head_a.next.next.value)  # Output: 3
print(head_b.value)  # Output: 1
print(head_b.next.value)  # Output: 5
print(head_b.next.next.value)  # Output: 6
# Output: List 1: 4 -> 2 -> 3 -> None
# Output: List 2: 1 -> 5 -> 6 -> None