#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'first_uniq_char' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import deque
def first_uniq_char(s):
    char_count = {}
    queue = deque()

    for i, char in enumerate(s):
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            queue.append(i)  

    while queue:
        index = queue.popleft()  
        if char_count[s[index]] == 1:
            return index

    return -1
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    arr = ast.literal_eval(input_data)

    result = first_uniq_char(arr)
    print(result)