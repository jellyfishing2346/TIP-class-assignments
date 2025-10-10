#!/bin/python

import math
import os
import random
import re
import sys
import ast

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_freq = {}
    t_freq = {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1

    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    return s_freq == t_freq

if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    input_list = ast.literal_eval(input_data)
    
    s = input_list[0]
    t = input_list[1]

    result = is_anagram(s, t)
    print(result)