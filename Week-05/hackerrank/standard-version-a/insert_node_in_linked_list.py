import math
import os
import random
import re
import sys

class ListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class LinkedList:
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

def print_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'insert' function below.
#
# The function is expected to return an INTEGER_LINKED_LIST.
# The function accepts following parameters:
#  1. INTEGER_LINKED_LIST head
#  2. INTEGER value
#  3. INTEGER position
#

def insert(head, value, position):
    # 1. Create the new node with the given value
    new_node = ListNode(value)

    # Case 1: Insertion at position 0 (new head)
    if position == 0:
        # The new node points to the current head
        new_node.next = head
        # The new node becomes the new head of the list
        return new_node

    # Case 2: Insertion in the middle or at the end
    
    # We need to find the node just *before* the target insertion point.
    # Start traversal from the head
    current = head
    
    # Loop 'position - 1' times to reach the node before the target position.
    # If the position is larger than the list length, the loop will naturally 
    # stop at the last node, resulting in insertion at the end.
    for _ in range(position - 1):
        # Stop if we reach the end of the list prematurely
        if current.next is None:
            break
            
        current = current.next

    # 'current' is now the node at index (position - 1) or the last node.
    
    # Step A: The new node points to the node that 'current' was previously pointing to.
    new_node.next = current.next
    
    # Step B: The 'current' node points to the new node, completing the insertion.
    current.next = new_node

    # Since the head did not change (position > 0), return the original head
    return head

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    input_line = input().strip()
    while(input_line != "END"):
           
        inputs = input_line.split(',')

        head = LinkedList()
        if len(inputs) == 3:
            try:
                head_count_str = inputs[0].strip()
                if head_count_str.startswith('ListNode(') and head_count_str.endswith(')'):
                    # This logic handles an unexpected single-node input format 
                    # but doesn't correctly handle a full list initialization.
                    # For a clean implementation, we assume the initial list is empty 
                    # and the test case provides an initial list *before* calling insert.
                    # Since the original problem context usually provides the list 
                    # elements, we will stick to the provided parsing logic:
                    
                    # Attempt to parse a single initial node value if in specific format
                    match = re.search(r'\d+', head_count_str)
                    if match:
                        head_value = int(match.group())
                        head.insert_node(head_value)
                    
                # The provided boilerplate seems incomplete for generating a full list.
                # Assuming 'head_count' was meant to loop and read list elements, 
                # but since they aren't provided in the input, we proceed with 
                # the current (likely partial) list generation logic.

                value = int(inputs[1].strip())
                position = int(inputs[2].strip())
            except (ValueError, IndexError):
                print("Invalid input format. Please provide a valid head_count, value, and position.")
                fptr.write('Invalid input format. Please provide a valid head_count, value, and position.\n')
                fptr.close()
                sys.exit(1)
        else:
            print("Invalid input format. Please provide exactly three values.")
            fptr.write('Invalid input format. Please provide exactly three values.\n')
            fptr.close()
            sys.exit(1)

        result = insert(head.head, value, position)
        print_linked_list(result, ' -> ', fptr)
        fptr.write('\n')
        input_line = input().strip()

    fptr.close()

#!/bin/python3