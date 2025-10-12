#!/bin/python

import math
import os
import random
import re
import sys
import ast 



#
# Complete the 'count_students_unable_to_eat' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY students
#  2. INTEGER_ARRAY sandwiches
#

def count_students_unable_to_eat(students, sandwiches):
    # Write your code here
    from collections import deque
    students = deque(students)
    sandwiches = list(sandwiches)
    total = 0
    while students and total < len(students): 
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.pop(0)
            total = 0
        else:
            students.append(students.popleft())
            total += 1
    return len(students)
    

if __name__ == '__main__':
    outfile = open(os.environ['OUTPUT_PATH'], 'w')
    input_data = sys.stdin.read().strip().splitlines()
    
    results = []
    
    for line in input_data:
        # Convert the line to list of lists
        students, sandwiches = eval(line)
        result = count_students_unable_to_eat(students, sandwiches)
        results.append(result)
    
    for res in results:
        outfile.write(str(res) + '\n')
    outfile.close()