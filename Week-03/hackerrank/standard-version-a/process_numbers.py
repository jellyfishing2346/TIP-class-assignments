from collections import deque

def process_numbers(nums):
    queue = deque([10, 20, 30])
    for num in nums:
        if num % 2 == 0:
            queue.append(num)
        elif queue and num % 2 != 0:
            queue.popleft()
    return list(queue)


nums = [2, 3, 4, 5, 6, 7]
print(process_numbers(nums)) # Output: [2, 4, 6]

