import math
import os
import random
import re
import sys
import ast

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        
# Helper function to print linked list (for testing)
def print_circular_linked_list(head):
    if not head:
        return
    current = head
    output = []
    while True:
        output.append(str(current.val))
        current = current.next
        if current == head:
            break
    print(" -> ".join(output))

#
# Complete the 'insert_into_sorted_circular_list' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER insert_val
#

#
# For your reference:
#
# ListNode:
#     int val
#     ListNode next
#
#

def insert_into_sorted_circular_list(head, insert_val):
    # Write your code here
    new_node = ListNode(insert_val)
    if not head:
        new_node.next = new_node
        return new_node

    current = head
    while True:
        nxt = current.next
        # normal case: insert between current and nxt
        if current.val <= insert_val <= nxt.val:
            new_node.next = nxt
            current.next = new_node
            break

        # boundary case: current is the max node and nxt is the min node
        if current.val > nxt.val:
            if insert_val >= current.val or insert_val <= nxt.val:
                new_node.next = nxt
                current.next = new_node
                break

        current = nxt
        # came full circle without finding a spot (all nodes equal, etc.)
        if current == head:
            # insert after head
            new_node.next = head.next
            head.next = new_node
            break

    return head

def parse_input(input_str):
    parts = input_str.split(', ')
    nodes_values = [int(x) for x in parts[0].split(' -> ')]
    insert_val = int(parts[1])

    if not nodes_values:
        return None, insert_val

    head = ListNode(nodes_values[0])
    current = head
    for value in nodes_values[1:]:
        current.next = ListNode(value)
        current = current.next
    current.next = head   

    return head, insert_val

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        head, insert_val = parse_input(input_data)

        result = insert_into_sorted_circular_list(head, insert_val)
        print_circular_linked_list(result)
        input_data = input()
