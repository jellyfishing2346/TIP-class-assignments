#!/bin/python3

import math
import os
import random
import re
import sys



def has_all_unique_characters(s):
    # Write your code here
    s_set = set(s)
    return len(s) == len(s_set)

if __name__ == "__main__":
    s = input().strip()
    result = has_all_unique_characters(s)
    print(result)