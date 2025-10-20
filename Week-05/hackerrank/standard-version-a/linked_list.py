import math
import os
import random
import re
import sys
import ast

class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

def print_linked_list(head):
    current = head
    while current:
        if current.next:
            sys.stdout.write(str(current.data) + " -> ")
        else:
            sys.stdout.write(str(current.data) + "\n")
        current = current.next

def create_linked_list(values):
    """
    Creates a singly linked list from a list of values.

    Args:
        values: A list of values to be stored in the linked list nodes.

    Returns:
        The head node of the newly created linked list.
    """
    if not values:
        # If the input list is empty, return None for an empty linked list
        return None

    # Initialize the head of the linked list with the first value
    head = Node(values[0])
    
    # Use a 'tail' pointer to easily append new nodes
    tail = head
    
    # Iterate through the rest of the values (starting from the second element)
    for value in values[1:]:
        # Create a new node
        new_node = Node(value)
        
        # Link the current tail's 'next' pointer to the new node
        tail.next = new_node
        
        # Move the tail pointer to the newly added node
        tail = new_node
        
    return head

if __name__ == '__main__':
    # The provided main execution logic is retained.
    # Note: In a real-world scenario where you execute this code block, 
    # it expects input from stdin and writes to the file path specified 
    # by the environment variable 'OUTPUT_PATH'.
    try:
        outfile = open(os.environ['OUTPUT_PATH'], 'w')
    except KeyError:
        # Fallback for local testing if OUTPUT_PATH is not set
        print("Warning: OUTPUT_PATH environment variable not set. Using 'output.txt' for outfile.")
        outfile = open('output.txt', 'w')
    except Exception as e:
        print(f"Error opening output file: {e}")
        sys.exit(1)
    
    def ll_to_str(head):
        list_str = ""
        curr = head
        while curr:
            list_str += str(curr.data)
            if curr.next:
                list_str += "->"
            curr = curr.next
        if len(list_str) == 0:
            return "None"
        return list_str
    
    print("Enter test cases (e.g., [1, 2, 3]) or 'END' to finish:")
    try:
        # Reading from sys.stdin might be more reliable in some environments than raw input()
        test_str = sys.stdin.readline().strip()
    except EOFError:
        test_str = "END" # Handle end-of-file for scripted input
        
    while(test_str != "END"):
        try:
            # Convert input string to list of param strings
            # ast.literal_eval is safer than eval() for parsing literals
            param_list = ast.literal_eval(test_str)
    
            result_raw = create_linked_list(param_list)
            result = ll_to_str(result_raw)
            
            # Write output and check for another test case
            outfile.write(str(result) + '\n')
            print(f"Input: {test_str}, Output: {result}") # Optional print for local testing
            
        except Exception as e:
            outfile.write(f"ERROR: {e} for input {test_str}\n")
            print(f"ERROR processing input {test_str}: {e}")
            
        try:
            test_str = sys.stdin.readline().strip()
        except EOFError:
            test_str = "END"

    outfile.close()
    print("Execution finished.")