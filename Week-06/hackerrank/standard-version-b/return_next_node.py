#!/usr/bin/env python3

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def mystery_function(head):
    if head is None:
        return None
    return head.next


if __name__ == '__main__':
    # build sample list: 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    out = mystery_function(head)

    # print the returned list
    vals = []
    cur = out
    while cur:
        vals.append(str(cur.value))
        cur = cur.next
    print(' -> '.join(vals))
    # Expected Output: 2 -> 3 -> 4
    # Time Complexity: O(1)
    # Space Complexity: O(1)
