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
    
# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    temp = ListNode()
    current = temp
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return temp.next

#
# Complete the 'longer_list' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_ARRAY head1
#  2. INTEGER_ARRAY head2
#
def get_length(head):
    total = 0
    current = head
    while current:
        total += 1
        current = current.next
    return total 

def longer_list(head1, head2):
    # Write your code here
    head1_length = get_length(head1)
    head2_length = get_length(head2)
    
    if head1_length >= head2_length:
        return head1
    else:
        return head2
    

if __name__ == '__main__':
    #input_data = sys.stdin.read().strip()
    #input_list = ast.literal_eval(input_data)
    
    #head1 = create_linked_list(input_list[0])
    #head2 = create_linked_list(input_list[1])

    #result = longer_list(head1, head2)
    #print_linked_list(result)
    
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Helper function to convert str -> linked list
    def str_to_ll(vals_str):
        if vals_str is None or vals_str == "None":
            return None
        vals = vals_str.split("->")
        temp_head = Node("temp")
        temp_curr = temp_head
        for val in vals:
            temp_curr.next = Node(val.strip())
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
        head1 = str_to_ll(param_list[0])
        head2 = str_to_ll(param_list[1])

        # TODO: Edit function name and prepare result string
        result_raw = longer_list(head1, head2) 
        result = ll_to_str(result_raw)
        
        # Write output and check for another test case
        outfile.write(str(result) + '\n')
        test_str = input()

    outfile.close()