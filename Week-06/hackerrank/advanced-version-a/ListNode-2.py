class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def merge(l1, l2):
    temp = ListNode(0)
    current = temp
    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return temp.next

# Time Complexity: O(n + m) where n and m are lengths of l1 and l2
# Space Complexity: O(1)