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

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(node, sep=' -> ', fptr=None):
    if node is None:
        if fptr:
            fptr.write('None\n')
        return 'None'
    
    result_str = []
    while node:
        result_str.append(str(node.data))
        node = node.next

    # Join the values with the separator and write to the file pointer
    if fptr:
        fptr.write(sep.join(result_str) + '\n')
    return sep.join(result_str)

#
# Complete the 'delete_node' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER value
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def delete_node(head, value):
    # Write your code here
    # Delete only the first occurrence of `value` and return the new head.
    if head is None:
        return None

    # If head needs to be deleted
    if head.data == value:
        return head.next

    prev = head
    curr = head.next
    while curr is not None:
        if curr.data == value:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the input string
    input_str = input().strip()
    while(input_str != "END"):
        # Extracting the integers from the input string
        all_values = re.findall(r'\d+', input_str)
        head = SinglyLinkedList()

        # Assume the input is space-separated integers followed by the value to be deleted
        if all_values:
            values = list(map(int, all_values[:-1]))
            delete_value = int(all_values[-1])

            # Insert all values as nodes
            for value in values:
                head.insert_node(value)

            # Delete the node with the specified value
            result_head = delete_node(head.head, delete_value)
        else:
            result_head = None  # No values, linked list is empty

        # Print the result using the updated function
        print_singly_linked_list(result_head, fptr=fptr)
        input_str = input().strip()

    fptr.close()