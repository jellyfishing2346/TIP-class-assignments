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
# Complete the 'count_nodes_with_value' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_SINGLY_LINKED_LIST head
#  2. INTEGER val
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def count_nodes_with_value(head, val):
    count = 0
    current = head

    while current.next: 
        if current.data == val:  
            count += 1
        current = current.next

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_data = input().strip()
    while(input_data != "END"):
        if input_data == "None":
            fptr.write(str(0))
            fptr.write('\n')
            input_data = input().strip()
        else:
            list_part, value_part = input_data.split(', ')  
        
            values = list(map(int, list_part.split(' -> ')))   

            value = int(value_part) 

            head = None
            tail = None

            for head_item in values:
                new_node = SinglyLinkedListNode(head_item)
                if head is None:
                    head = new_node   
                    tail = head
                else:
                    tail.next = new_node   
                    tail = new_node   

            result = count_nodes_with_value(head, value) 
            fptr.write(str(result))
            fptr.write('\n')
            input_data = input().strip()
    fptr.close()