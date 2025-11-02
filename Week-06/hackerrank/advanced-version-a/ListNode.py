class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_node(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# Time Complexity: O(n)
# Space Complexity: O(1)