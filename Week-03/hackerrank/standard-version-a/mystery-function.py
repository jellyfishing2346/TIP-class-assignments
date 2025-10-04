def mystery_function(nums):
    left = len(nums) - 1
    right = len(nums) - 1

    while right >= 0:
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left -= 1
        right -= 1
    return nums

nums = [0, 0, 1, 2, 0, 3]
print(mystery_function(nums)) # Output: [0, 0, 0, 1, 2, 3]