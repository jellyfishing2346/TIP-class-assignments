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

    def insert_node(self, node_data):
        node = ListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        
# Helper function to convert list to linked list
def list_to_linkedlist(lst):
    temp = ListNode()
    current = temp
    for value in lst:
        current.next = ListNode(val=value)
        current = current.next
    return temp.next

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        if current.next:
            print(current.val),  # Note the comma for Python 2 to avoid newline
            print("->"),
        else:
            print(current.val)
        current = current.next
        
def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.val))  # Changed from node.data to node.val
        node = node.next
        if node:
            fptr.write(sep)

#
# Complete the 'middle_node' function below.
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

def middle_node(head):
    # Write your code here
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    linked_list_input = input().strip()   
    while(linked_list_input != "END"):
        skip = 0
        if linked_list_input == "" or linked_list_input == '""':
            fptr.write("None\n")
            linked_list_input = input().strip()   
        else:
            try:
                head_items = list(map(int, linked_list_input.split(' -> ')))
            except ValueError:
                fptr.write("None\n")
                skip = 1
                linked_list_input = input().strip()
            
            if skip == 0:
                head = SinglyLinkedList()

                for head_item in head_items:
                    head.insert_node(head_item)

                result = middle_node(head.head)

                print_singly_linked_list(result, ' -> ', fptr)
                fptr.write('\n')
                linked_list_input = input().strip()

    fptr.close()