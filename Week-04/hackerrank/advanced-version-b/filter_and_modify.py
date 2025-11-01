from collections import deque

def filter_and_modify(nums):
    queue = deque()
    for num in nums:
        if num % 2 == 0:
            queue.append(num * 2)
        elif num > 10 and queue:
            queue.popleft()
    return list(queue)
print(filter_and_modify([2, 12, 4, 14, 6, 5]))  # Example usage
# Output should be [4, 24, 8, 28, 12]