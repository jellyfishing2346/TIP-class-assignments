#!/bin/python3

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

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(node.data)

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'create_linked_list' function below.
#
# The function is expected to return a STRING_SINGLY_LINKED_LIST.
# The function accepts INTEGER_ARRAY values as parameter.
#

def create_linked_list(values):
    if not values:
        return None
    
    head = SinglyLinkedListNode(values[0])
    current = head
    # 2. Iterate over the remaining values
    for value in values[1:]:
        # FIX 1: Correctly use the loop variable 'value' for the node data
        new_node = SinglyLinkedListNode(value) 
        
        # 3. Link the new node to the end of the current list segment
        current.next = new_node
        
        # FIX 2: Advance the 'current' pointer to the newly added node
        current = new_node 
        
    return head

def format_linked_list(node):
    if node is None:
        return 'None'
    result = []
    while node:
        result.append(str(node.data))
        node = node.next
    return ' -> '.join(result)
    
if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        values = ast.literal_eval(input_data)

        result = create_linked_list(values)
        print(format_linked_list(result))
        input_data = input()