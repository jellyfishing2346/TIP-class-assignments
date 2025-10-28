#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'power' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER n
#

def power(x, n):
    # Write your code here
    if n == 0:
        return 1
    elif n > 0: 
        return x * power(x, n - 1)
    else:
        return 1 / power(x, abs(n))