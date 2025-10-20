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

def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.val) + " -> ")
        else:
            sys.stdout.write(str(current.val) + "\n")
        current = current.next



#
# Complete the 'create_linked_list' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_ARRAY values as parameter.
#

def create_linked_list(values):
    # Step #1: Check if the list is empty if so return None
    if not values: 
        return None
    
    # Step #2: Set the head node to the first value in the linked list
    head = ListNode(values[0])
    # Step #3: Create a current pointer to keep of the head pointer's positions until it reaches the end
    current = head
    
    # Step #4: Go through the rest of the list starting with the second value in the list
    for m in values[1:]:
        # Create a new node to be apart of the linked list
        new_node = ListNode(m)
        # Place the new node after the current node's position
        current.next = new_node
        # Have the current node be the new node
        current = new_node
    
    # Once finished returned the revised head of the new linked list
    return head
    
    
        

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    
    def ll_to_str(head):
        list_str = ""
        curr = head
        while curr:
            list_str += str(curr.val)
            if curr.next:
                list_str += " -> "
            curr = curr.next
        if len(list_str) == 0:
            return "None"
        return list_str
    
    input_data = input()
    while(input_data != "END"):
        param_list = ast.literal_eval(input_data)
        result_raw = create_linked_list(param_list)
        result = ll_to_str(result_raw)
        outfile.write(str(result) + '\n')
        input_data = input()
    outfile.close()