#!/bin/python

import math
import os
import random
import re
import sys
import ast

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

# Helper function to print linked list (for testing)
def print_linked_list(head):
    if head is None:
        return 'None'   
    
    current = head
    output = []
    while current:
        output.append(str(current.data))
        current = current.next
    return ' -> '.join(output)
    
def list_to_linked_list(lst):
    linked_list = SinglyLinkedList()
    for item in lst:
        linked_list.insert_node(item)
    return linked_list.head

# Complete the 'merge_two_lists' function below.


def merge_two_lists(l1, l2):
    
    # Merge two sorted singly-linked lists and return head of merged list.
    dummy = SinglyLinkedListNode(0)
    tail = dummy
    a, b = l1, l2
    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    # attach remaining
    tail.next = a if a else b
    return dummy.next

