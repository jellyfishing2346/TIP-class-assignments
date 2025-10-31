def recursive_helper(index, stack, arr):
    # Base Case: Stop when we've processed all elements in arr
    if index == len(arr):
        return 0

    # 1. Push the current array element onto the stack
    stack.append(arr[index])

    # 2. Pop the last element pushed (which is the current element)
    result = stack.pop() + \
             recursive_helper(index + 1, stack, arr) # Recursive Call

    # 3. Return the calculated result
    return result

def mystery_function(arr):
    # Initialize an empty list to be used as a stack
    stack = []
    # Start the helper function at index 0
    return recursive_helper(0, stack, arr)

print(mystery_function([10, 20, 30]))
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack and auxiliary stack