#!/bin/python

import math
import os
import random
import re
import sys
import ast

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

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
# Complete the 'traverse_linked_list' function below.
#
# The function is expected to return an integer array.
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

def traverse_linked_list(head):
    # Write your code here
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


import ast

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Helper function to convert str -> linked list
    def str_to_ll(vals_str):
        if vals_str is None or vals_str == "None" or vals_str == '':
            return None
        vals = vals_str.split("->")
        temp_head = Node("temp")
        temp_curr = temp_head
        for val in vals:
            temp_curr.next = Node(int(val.strip()))
            temp_curr = temp_curr.next
        return temp_head.next #Don't keep the temp head

    # Helper function to convert linked list -> str
    def ll_to_str(head):
        list_str = ""
        curr = head
        while curr:
            list_str += str(curr.val)
            if curr.next:
                list_str += "->"
            curr = curr.next
        if len(list_str) == 0:
            return "None"
        return list_str
        
    test_str = input()
    while(test_str != "END"):
        # Convert input string to list of param strings
        param_list = ast.literal_eval(test_str)

        # TODO: Edit parameters as needed
        test_ll = str_to_ll(param_list[0])

        # TODO: Edit function name and prepare result string
        result_raw = traverse_linked_list(test_ll)
        result = str(result_raw)
        
        # Write output and check for another test case
        outfile.write(result + '\n')
        test_str = input()

    outfile.close()