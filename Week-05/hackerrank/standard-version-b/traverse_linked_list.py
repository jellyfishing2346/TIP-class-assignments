#!/bin/python

import math
import os
import random
import re
import sys

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
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



#
# Complete the 'traverse_linked_list' function below.
#
# The function is expected to return an INTEGER_ARRAY.
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

def traverse_linked_list(head):
    # Write your code here
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Sample input string directly (replace with raw_input() as needed)
    # Use input() to read from standard input
    input_str = input().strip()
    while(input_str != "END"):

        # Extracting the integers from the input string
        values = re.findall(r'\d+', input_str)
        linked_list = SinglyLinkedList()

        for value in values:
            linked_list.insert_node(int(value))

        result = traverse_linked_list(linked_list.head)

        fptr.write('[{}]\n'.format(', '.join(map(str, result))))
        input_str = input().strip()
        
    fptr.close()
