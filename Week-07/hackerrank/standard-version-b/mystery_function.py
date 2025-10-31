def mystery_function(arr):
    if not arr:
        return 1
    return arr[0] * mystery_function(arr[1:])

print(mystery_function([2, 3, 4]))  # Output: 24
print(mystery_function([1, 5, 6, 2])) # Output: 60
# Time Complexity: O(n)