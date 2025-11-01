def mystery_function(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + mystery_function(arr, n - 1)

arr = [1, 2, 3, 4, 5]
print(mystery_function(arr, len(arr)))  # Output: 15