
#!/bin/python

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

# Debug the function below

def delete_node(head, key):
    if head is None:
        return None

    # Case 1: The head node is the node to be deleted.
    if head.data == key:
        # Move the head pointer to the next node and return the new head.
        return head.next

    # Case 2: The node to be deleted is not the head (somewhere in the middle or end).
    prev = head
    curr = head.next

    while curr:
        if curr.data == key:
            # Bypass the current node (curr)
            prev.next = curr.next
            break
        
        # Move pointers forward
        prev = curr
        curr = curr.next

    # If the key was not found, the list remains unchanged, and the original head is returned.
    return head

import sys

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = SinglyLinkedListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = SinglyLinkedListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list back to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    return result

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    results = []

    for line in input_data:
        values, key = eval(line)  # Parse input as a list of values and a key
        head = create_linked_list(values)
        updated_head = delete_node(head, key)
        results.append(linked_list_to_list(updated_head))

    for res in results:
        print(res)