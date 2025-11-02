#!/bin/python

import math
import os
import random
import re
import sys
import ast

class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

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
        
# Helper function to convert list to linked list       
def list_to_linkedlist(lst):
    temp = ListNode(0)  # Initialize with a dummy node
    current = temp
    for value in lst:
        # ListNode constructor takes a single value argument
        current.next = ListNode(value)
        current = current.next
    return temp.next

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        if current.next:
            print(current.data, "->", end=" ")
        else:
            print(current.data)
        current = current.next


#
# Complete the 'linked_list_frequencies' function below.
#
# The function is expected to return an INTEGER_ARRAY.
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

def linked_list_frequencies(head):
    # Write your code here
    freq_map = {}
    current = head
    while current:
        if current.data in freq_map:
            freq_map[current.data] += 1
        else:
            freq_map[current.data] = 1
        current = current.next
    # Return a dictionary mapping node values to their frequencies.
    return freq_map

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the entire input as a string and convert it to a list
    input_data = input().strip()  # Use input() instead of raw_input() in Python 3
    while(input_data != "END"):
        head_items = ast.literal_eval(input_data)  # Safely evaluate the input string

        head = SinglyLinkedList()

        for head_item in head_items:
            head.insert_node(head_item)

        result = linked_list_frequencies(head.head)

        # Write the frequencies to the output
        fptr.write(str(result) + '\n')
        input_data = input().strip()
    
    fptr.close()