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
# Complete the 'swap_pairs' function below.
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

def swap_pairs(head):
    if not head or not head.next:
        return head
    new_head = head.next
    prev = None
    current = head

    while current and current.next:
        next_pair = current.next.next
        current.next.next = current
        if prev:
            prev.next = current.next
        current.next = next_pair
        prev = current
        current = next_pair

    return new_head


def parse_linked_list(input_str):
    values = list(map(int, input_str.split(' -> ')))
    linked_list = SinglyLinkedList()
    for value in values:
        linked_list.insert_node(value)
    return linked_list.head

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        linked_list = parse_linked_list(input_data)

        result = swap_pairs(linked_list)
        print_linked_list(result)
        input_data = input()