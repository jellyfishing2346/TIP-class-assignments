def process_numbers(nums, threshold):
    stack = []
    for num in nums:
        if num < threshold:
            stack.append(num)
        elif num <= 10 and stack:
            stack.pop()
    return stack

print(process_numbers([3, 5, 1, 9, 6, 15], 8)) # Output: [3, 5, 1, 6]