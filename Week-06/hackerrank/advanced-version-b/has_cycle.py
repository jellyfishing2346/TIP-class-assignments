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
 

#
# Complete the 'has_cycle' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.
#

#
# For your reference:
#
# ListNode:
#     int value
#     ListNode next
#
#

def has_cycle(head):
    # Write your code here
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def build_linked_list(values):
    linked_list = SinglyLinkedList()
    for value in values:
        linked_list.insert_node(value)
    return linked_list.head

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        values = list(map(int, input_data.replace('->', '').split()))
        
        linked_list_head = build_linked_list(values)

        if linked_list_head and linked_list_head.next and linked_list_head.next.next:
            linked_list_head.next.next.next = linked_list_head.next 

        result = has_cycle(linked_list_head)
        print(result)
        input_