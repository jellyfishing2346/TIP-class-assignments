def mystery_function(arr):
    if not arr:
        return 0
    return arr[0] + mystery_function(arr[1:])

print(mystery_function([1, 2, 3, 4, 5]))  # Output: 15
print(mystery_function([10, 20, 30]))     # Output: 60