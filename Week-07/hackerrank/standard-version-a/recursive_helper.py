from collections import deque

def recursive_helper(queue):
    if not queue:
        return 0
    else:
        element = queue.popleft()
        return element + recursive_helper(queue)

def sum_with_queue(arr):
    queue = deque(arr)
    return recursive_helper(queue)

print(sum_with_queue([1, 2, 3, 4, 5]))  # Output: 15