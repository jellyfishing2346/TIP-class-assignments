def mystery_function(n):
    if n == 0 or n == 1:
        return 1
    return n * mystery_function(n - 1)
# Time complexity: O(n)
# Space complexity: O(n) due to recursion stack
