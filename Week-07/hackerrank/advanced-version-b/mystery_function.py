def mystery_function(arr, n):
    if n == 0:
        return 0
    last_value = arr[n - 1] if arr[n - 1] % 2 == 0 else 0
    return last_value + mystery_function(arr, n - 2)
# Time Complexity: O(n/2) => O(n)
# Space Complexity: O(n) due to recursion stack