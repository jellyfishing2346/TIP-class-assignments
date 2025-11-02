class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def concatenate_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1
    current = list1
    while current.next:
        current = current.next
    current.next = list2
    return list1
# Time Complexity: O(n + m)
# Space Complexity: O(1)