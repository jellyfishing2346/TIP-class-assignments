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
def print_linked_list(head):
    if head is None or head == '':
        sys.stdout.write("\n")
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next

#
# Complete the 'reverse_between' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER left
#  3. INTEGER right
#

#
# For your reference:
#
# ListNode:
#     int val
#     ListNode next
#
#

def reverse_between(head, left, right):
    # Write your code here
    if not head or left == right:
        return head

    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move `prev` to the node before the `left` position
    for _ in range(left - 1):
        prev = prev.next

    # Reverse the sublist from `left` to `right`
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next

def parse_input(input_data):
    # Parse the linked list part
    if not input_data.strip():  # Check if the input is empty or only whitespace
        return None, 0, 0

    parts = input_data.split(', ')
    
    if len(parts) != 3 or parts[0].strip() == '':
        return None, 0, 0  # If there is no linked list data, return None for head and 0 for left/right

    linked_list_str, left, right = parts
    left = int(left)
    right = int(right)
    
    # Create the linked list
    linked_list_values = list(map(int, linked_list_str.split(' -> ')))

    sll = SinglyLinkedList()
    for val in linked_list_values:
        sll.insert_node(val)
    
    return sll.head, left, right

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        head, left, right = parse_input(input_data)

        result = reverse_between(head, left, right)
        print_linked_list(result)
        input_data = input()