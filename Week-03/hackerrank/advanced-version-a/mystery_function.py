def mystery_function(nums):
    if not nums:
        return 0 
    
    left = 0
    
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]
    return left + 1

# Test case
result = mystery_function([1, 1, 2, 2, 2, 3, 4, 4, 5])
print(result)