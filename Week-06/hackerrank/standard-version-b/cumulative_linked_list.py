#!/usr/bin/env python3

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def mystery_function(head):
    if not head:
        return None

    total = 0
    current = head

    while current:
        total += current.value
        current.value = total
        current = current.next

    return head


if __name__ == '__main__':
    # construct list: 1 -> 2 -> 3 -> 4
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    out = mystery_function(head)

    # print result
    vals = []
    cur = out
    while cur:
        vals.append(str(cur.value))
        cur = cur.next
    print(' -> '.join(vals))
