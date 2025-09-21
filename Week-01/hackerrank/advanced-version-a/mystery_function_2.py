def mystery_function(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] > 0:  # Check if the number is positive
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
        if count > max_count:
            max_count = count
    return max_count

result = mystery_function([1, 2, -3, 4, 5, -6, 7, 8, 9])
print(result)  # Output: 3