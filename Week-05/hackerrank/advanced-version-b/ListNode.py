class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def is_palindrome(head):
    # Check if a singly linked list is a palindrome.
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values == values[::-1]
# Example usage:
# Input: 1 -> 2 -> 2 -> 1
# Output: True
# Time Complexity: O(n)
# Space Complexity: O(n) due to the list used to store values