#!/bin/python

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

    def insert_node(self, node_data):
        node = ListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))  

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse_list' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def reverse_list(head):
    # Write your code here
    prev = None
    current = head
    while current:
        next_node = current.next  # Store next node
        current.next = prev       # Reverse the link
        prev = current            # Move prev to current
        current = next_node       # Move to next node
    return prev  # New head of the reversed list

def parse_linked_list(input_data):
    # Handle empty input
    if not input_data.strip():
        return []
    
    # Split the input and convert to integers
    nodes = input_data.split(' -> ')
    return [int(node) for node in nodes if node.isdigit()]

if __name__ == '__main__':
    input_data = input().strip()  # Read the full input
    while(input_data != "END"):
        linked_list_data = parse_linked_list(input_data)  # Parse the input
        
        linked_list = SinglyLinkedList()  # Create an instance of SinglyLinkedList
        for item in linked_list_data:
            linked_list.insert_node(item)  # Insert each item into the linked list
        
        result = reverse_list(linked_list.head)  # Reverse the linked list

        # Print the reversed linked list
        output = []
        while result:
            output.append(str(result.val))  # Collect values from the reversed list
            result = result.next

        print(" -> ".join(output))  # Print as required format
        input_data = input().strip()