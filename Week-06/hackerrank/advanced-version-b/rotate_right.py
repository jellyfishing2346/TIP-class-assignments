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

    def insert_node(self, val):
        node = ListNode(val)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        
# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next

#
# Complete the 'rotate_right' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER k
#

#
# For your reference:
#
# ListNode:
#     int val
#     ListNode next
#
#

def rotate_right(head, k):
    # Write your code here
    if not head or k == 0:
        return head
    # Compute the length of the list and get the tail node
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1
    # Connect the tail to the head to make it circular
    tail.next = head
    # Find the new head after rotation
    k = k % length
    steps_to_new_head = length - k
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        list_part, k_part = input_data.split(", ")
        
        values = list(map(int, list_part.split(" -> ")))
        k = int(k_part)  

        linked_list = SinglyLinkedList()
        for value in values:
            linked_list.insert_node(value)

        result = rotate_right(linked_list.head, k)

        print_linked_list(result)
        input_data = input()