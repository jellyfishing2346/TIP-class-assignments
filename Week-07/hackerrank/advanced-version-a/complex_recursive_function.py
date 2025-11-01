def complex_recursive_function(arr, multiplier):
    if not arr:
        return 1
    return arr[0] * multiplier + complex_recursive_function(arr[1:], multiplier)

print(complex_recursive_function([1, 2, 3], 2))  # Output: 13
print(complex_recursive_function([4, 5], 3))     # Output: 28