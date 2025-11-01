#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'find_smallest_index' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. Node tail
#  2. int val
#
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

def find_smallest_index(tail, val):
    # Given the tail of a doubly-linked list, find the smallest index
    # (0-based from the head) of the first node whose value equals `val`.
    # If not found, return -1.
    if tail is None:
        return -1

    # Collect values from tail back to head
    vals_from_tail = []
    cur = tail
    while cur:
        vals_from_tail.append(cur.val)
        cur = cur.prev

    # vals_from_tail is [tail_val, ..., head_val]; reverse to get head->tail
    vals = vals_from_tail[::-1]
    try:
        return vals.index(val)
    except ValueError:
        return -1

import ast
if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    
    # Helper function to convert str -> linked list
    def str_to_dll(vals_str):
        if vals_str is None or vals_str == "None":
            return None
        vals = vals_str.split("<->")
        temp_head = Node("temp")
        temp_curr = temp_head
        for val in vals:
            temp_curr.next = Node(int(val.strip()))
            temp_curr.next.prev = temp_curr # DLL
            temp_curr = temp_curr.next
        head = temp_head.next
        head.prev = None
        return head, temp_curr # head, tail

    # Helper function to convert linked list -> str
    def dll_to_str(head):
        list_str = ""
        curr = head
        while curr:
            list_str += str(curr.val)
            if curr.next:
                list_str += "<->"
            curr = curr.next
        if len(list_str) == 0:
            return "None"
        return list_str
        
    test_str = input()
    while(test_str != "END"):
        # Convert input string to list of param strings
        param_list = ast.literal_eval(test_str)

        # TODO: Edit parameters as needed
        test_head, test_tail = str_to_dll(param_list[0])
        val = int(param_list[1])

        # TODO: Edit function name and prepare result string
        result_raw = find_smallest_index(test_tail, val) 
        result = str(result_raw) + "|" + dll_to_str(test_head)
        
        # Write output and check for another test case
        outfile.write(str(result) + '\n')
        test_str = input()

    outfile.close()