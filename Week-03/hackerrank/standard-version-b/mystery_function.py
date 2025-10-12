def mystery_function(nums):
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
            left += 1
        right += 1
    return nums
print(mystery_function([0,0,1,2,0,3])) # Output: [1,2,3,0,0,0]

