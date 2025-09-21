#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'get_top_player' function below.
#
# The function is expected to return a STRING.
#

def get_top_player(dictionary):
    high_score = float('-inf')
    top_player = ""
    for name, score in dictionary.items():
        if score > high_score:
            high_score = score
            top_player = name
    return top_player
if __name__ == '__main__':
    input_data = sys.stdin.read().strip()
    dictionary = ast.literal_eval(input_data)

    result = get_top_player(dictionary)
    print(result)