#!/bin/python

import math
import os
import random
import re
import sys
import ast

class DoublyLinkedListNode:
    def __init__(self, node_value):
        self.value = node_value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_value):
        node = DoublyLinkedListNode(node_value)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.value))   

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'find_smallest_index' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_DOUBLY_LINKED_LIST tail
#  2. INTEGER val
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int val
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

def find_smallest_index(tail, val):
    # --- Step 1: Find the head of the list ---
    # We start at the tail and move backward until we hit the first node (where .prev is None)
    head = tail
    while head.prev:
        head = head.prev
        
    # --- Step 2: Traverse forward from the head to find the SMALLEST index ---
    current = head
    index = 0
    
    while current:
        if current.val == val:
            # Found the value! Since we are moving forward (from index 0, 1, 2...),
            # this is guaranteed to be the smallest index.
            return index
            
        current = current.next
        index += 1
        
    # If the loop completes without finding the value
    return -1

import ast
if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Helper function to convert str -> linked list
    def str_to_dll(vals_str):
        if vals_str is None or vals_str == "None":
            return None
        vals = vals_str.split("<->")
        temp_head = Node("temp")
        temp_curr = temp_head
        for val in vals:
            temp_curr.next = Node(int(val.strip()))
            temp_curr.next.prev = temp_curr # DLL
            temp_curr = temp_curr.next
        head = temp_head.next
        head.prev = None
        return head, temp_curr # head, tail

    # Helper function to convert linked list -> str
    def dll_to_str(head):
        list_str = ""
        curr = head
        while curr:
            list_str += str(curr.val)
            if curr.next:
                list_str += "<->"
            curr = curr.next
        if len(list_str) == 0:
            return "None"
        return list_str
        
    test_str = input()
    while(test_str != "END"):
        # Convert input string to list of param strings
        param_list = ast.literal_eval(test_str)

        # TODO: Edit parameters as needed
        test_head, test_tail = str_to_dll(param_list[0])
        val = int(param_list[1])

        # TODO: Edit function name and prepare result string
        result_raw = find_smallest_index(test_tail, val) 
        result = str(result_raw) + "|" + dll_to_str(test_head)
        
        # Write output and check for another test case
        outfile.write(str(result) + '\n')
        test_str = input()

    outfile.close()