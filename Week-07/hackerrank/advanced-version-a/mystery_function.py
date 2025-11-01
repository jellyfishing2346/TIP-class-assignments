def mystery_function(arr, left, right):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] < arr[right]:
        return mystery_function(arr, right, mid + 1)
    else:
        return mystery_function(arr, left, mid - 1)

# Time Complexity: O(log n)
# Space Complexity: O(log n) due to recursion stack