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

# Helper function to print linked list (for testing)
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next



def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# Function to convert the input string into a linked list
def build_linked_list_from_string(input_data: str) -> SinglyLinkedListNode:
    elements = list(map(int, input_data.split(" -> ")))
    linked_list = SinglyLinkedList()
    for element in elements:
        linked_list.insert_node(element)
    return linked_list.head

if __name__ == '__main__':
    input_data = input()
    while (input_data != "END"):
        head = build_linked_list_from_string(input_data)

        result = reverse_linked_list(head)
        print_linked_list(result)
        input_data = input()