class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def mystery_function(head):
    array =[]
    current = head
    while current:
        array.append(current.value)
        current = current.next
    return array
# Time Complexity: O(n)
# Space Complexity: O(n)