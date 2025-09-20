import sys
import ast

def reverse_lst(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst

if __name__ == '__main__':
    input_str = sys.stdin.read().strip()
    # Convert the input string to a list of integers
    input_list = ast.literal_eval(input_str)
    # Reverse the list
    result = reverse_lst(input_list)
    # Print the reversed list
    print(result)