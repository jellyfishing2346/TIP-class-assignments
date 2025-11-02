class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
def remove_duplicates(head):
    if not head:
        return head
    
    # Remove duplicates from a sorted singly linked list.
    current = head
    seen = set([current.value])
    while current.next:
        if current.next.value in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.value)
            current = current.next
    return head

# Example usage:
# Input: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
# Output: 1 -> 2 -> 3 -> 4 -> 5
# Time Complexity: O(n)
# Space Complexity: O(n) due to the set used to track seen values