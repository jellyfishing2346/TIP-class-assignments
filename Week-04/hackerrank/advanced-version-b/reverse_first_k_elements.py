#!/bin/python3

import math
import os
import random
import re
import sys
import ast
from collections import deque

#
# Complete the 'reverse_first_k_elements' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY queue
#  2. INTEGER k
#

def reverse_first_k_elements(queue, k):
    if k > len(queue) or k <= 0:
        return queue
    
    stack = []
    for _ in range(k):
        stack.append(queue.popleft())
    
    while stack:
        queue.append(stack.pop())
    
    for _ in range(len(queue) - k):
        queue.append(queue.popleft())
    
    return queue

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_data)
    
    queue = deque(input_list[0])  # Convert list to deque
    k = input_list[1]

    result = reverse_first_k_elements(queue, k)
    
    for val in result:
        print(val)