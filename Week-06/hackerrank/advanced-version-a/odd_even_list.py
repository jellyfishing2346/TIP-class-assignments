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

    def get_head(self):
        return self.head
   
        
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
# Complete the 'odd_even_list' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# ListNode:
#     int val
#     ListNode next
#
#

def odd_even_list(head):
    # Write your code here
    if head is None:
        return None
    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head
    return odd_head

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        values = list(map(int, re.split(r' -> ', input_data)))

        linked_list = SinglyLinkedList()
        for value in values:
            linked_list.insert_node(value)

        result_head = odd_even_list(linked_list.get_head())
        print_linked_list(result_head)
        input_data = input()