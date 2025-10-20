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


# Function to insert a node into a sorted linked list
def insert_sorted(head, value):
    new_node = ListNode(value)
    
    # Step #1: Check if the list is empty or if the new value is bigger than the head node's value
    if head is None or value < head.val:
        new_node.next = head
        return new_node
    
    # Step #2: Tranverse the linked list to find the correct insertion spot
    current = head
    while current.next is not None and current.next.val < value:
        current = current.next
        
    # Step #3: Insert the new node
    new_node.next = current.next
    
    # Set the current.next pointer to the new node
    current.next = new_node
    
    # Step #4: Return the newly updated head
    return head

import sys

# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert linked list to a list
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    results = []

    for line in input_data:
        values, value = eval(line)  # Parse input as list of values and a new value
        head = create_linked_list(values)
        updated_head = insert_sorted(head, value)
        results.append(linked_list_to_list(updated_head))

    for res in results:
        print(res)