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

    def insert_node(self, node_data):
        node = ListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.val))  

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse_list_recursively' function below.
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

def reverse_list_recursively(head):
    # Recursive reverse of a singly linked list.
    # Base case: empty or single node
    if head is None or head.next is None:
        return head

    # Recursively reverse the rest
    new_head = reverse_list_recursively(head.next)

    # head.next is now the tail of the reversed sublist
    head.next.next = head
    head.next = None

    return new_head

def parse_linked_list(input_data):
    if input_data == '[]':
        return []  
    nodes = input_data.strip('[]').split(', ')
    return [int(node) for node in nodes if node] 

if __name__ == '__main__':
    input_data = sys.stdin.read().strip().splitlines()  
    
    for data in input_data:   
        if data:   
            linked_list_data = parse_linked_list(data)   
            
            linked_list = SinglyLinkedList()  
            for item in linked_list_data:
                linked_list.insert_node(item)   
            
            result = reverse_list_recursively(linked_list.head)  
            output = []
            while result:
                output.append(str(result.val))   
                result = result.next
            
            print(" -> ".join(output))  