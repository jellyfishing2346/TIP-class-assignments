def mystery_function(height):
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        max_water = max(max_water, width * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water

# Test case
result = mystery_function([1,8,6,2,5,4,8,3,7])
print(result)  # Expected output: 49