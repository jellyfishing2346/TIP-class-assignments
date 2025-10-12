def process_numbers(nums):
    stack = [1]
    for num in nums:
        if num % 2 == 0:
            stack.append(num)
        elif stack and num % 2 != 0:
            stack.pop()
    return stack

nums = [2,3,4,5,6,7]
print(process_numbers(nums)) # Output: [1]