#!/bin/python

import math
import os
import random
import re
import sys

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




def remove_duplicates(head: ListNode) -> ListNode:
    if not head:
        return None  
    
    current = head
    while current.next: 
        if current.val == current.next.val:  
            current.next = current.next.next  
        else:
            current = current.next  
    
    return head

import sys

def parse_input():
    """
    Reads multiple lines of input, where each line represents a separate linked list.
    Returns a list of ListNode heads, one for each linked list.
    """
    lines = sys.stdin.read().strip().split("\n")  # Read all lines separately
    linked_lists = []

    for line in lines:
        if not line.strip():  # Handle empty lines (edge case)
            linked_lists.append(None)
            continue

        values = line.strip().split(" -> ")  # Split the linked list values
        nodes = [ListNode(int(val)) for val in values]
        
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]  # Link nodes together

        linked_lists.append(nodes[0])  # Store the head of the linked list

    return linked_lists  # Return a list of linked lists

def print_linked_list(head):
    """
    Prints the linked list in the required format.
    """
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

if __name__ == "__main__":
    heads = parse_input()  # Get all linked list heads

    for head in heads:  # Process each linked list separately
        new_head = remove_duplicates(head)
        print_linked_list(new_head)  # Print each modified list on a new line