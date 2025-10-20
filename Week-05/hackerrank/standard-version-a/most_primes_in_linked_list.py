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

# Helper function to create a linked list from a list of values
def create_linked_list(vals):
    temp = SinglyLinkedListNode(0)  # Dummy node
    current = temp
    for val in vals:
        current.next = SinglyLinkedListNode(val)
        current = current.next
    return temp.next

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Complete the 'most_primes_list' function below.
#
# The function is expected to return a SinglyLinkedListNode.
# The function accepts two SinglyLinkedListNode parameters: head_a and head_b.
#
def most_primes_list(head_a, head_b):
    def count(head):
        total = 0
        current = head
        while current:
            if is_prime(current.data):
                total += 1
            current = current.next
        return total
        
    # Count primes in list A
    a_primes = count(head_a)
    # Count primes in list B
    b_primes = count(head_b)
    
    # Check to see if list A has more primes than list B
    if a_primes >= b_primes:
        # CORRECT: Return the head node of list A
        return head_a 
    else:
        # CORRECT: Return the head node of list B
        return head_b
    
            

import sys

# Helper function to print linked list
def print_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))
        node = node.next
        if node:
            fptr.write(sep)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    try:
        input_data = sys.stdin.read().strip().split("\n")  # Read all input at once
    except EOFError:
        input_data = []

    for line in input_data:
        if not line.strip():
            continue
        
        try:
            # Parse input as list of lists
            input_list = ast.literal_eval(line)  

            if not isinstance(input_list, list) or len(input_list) != 2:
                raise ValueError("Input must be a list of two lists.")

            head_a = create_linked_list(input_list[0])
            head_b = create_linked_list(input_list[1])

            result = most_primes_list(head_a, head_b)
            print_linked_list(result, ' -> ', fptr)
            fptr.write('\n')

        except Exception as e:
            # Handle potential parsing or processing errors
            # print(f"Error processing input line '{line}': {e}", file=sys.stderr)
            pass # Keep silent for submission environment

    fptr.close()