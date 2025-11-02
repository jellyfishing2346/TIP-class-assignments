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
    current = head
    while current:
        if current.next:
            print(current.data),
            print(" -> "),
        else:
            print(current.data)
        current = current.next



#
# Complete the 'is_palindrome' function below.
#
# The function is expected to return a BOOLEAN.
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

def is_palindrome(head):
    # Write your code here
    # Check if a singly linked list is a palindrome.
    values = []
    current = head
    while current:
        values.append(current.data)
        current = current.next
    return values == values[::-1]


def parse_linked_list(input_data):
    # Handle empty input
    if not input_data.strip():
        return []
    
    # Split the input and convert to integers
    nodes = input_data.split(' -> ')
    return [int(node) for node in nodes if node.isdigit()]

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    
    input_data = input().strip()
    while(input_data != "END"):
        linked_list_data = parse_linked_list(input_data)
        
        linked_list = SinglyLinkedList()
        for item in linked_list_data:
            linked_list.insert_node(item)
        
        result = is_palindrome(linked_list.head)
        outfile.write(str(result) + '\n')
        input_data = input().strip()

    outfile.close()