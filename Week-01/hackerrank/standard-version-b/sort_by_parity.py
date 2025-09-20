def sort_by_parity(nums):
    evens = []
    odds = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds

print(sort_by_parity([3,1,2,4])) # Output: [2, 4, 3, 1]