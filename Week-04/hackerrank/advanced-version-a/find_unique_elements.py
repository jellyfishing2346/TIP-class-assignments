def find_unique_elements(arr):
    unique_elements = set()
    for num in arr:
        unique_elements.add(num)
    return list(unique_elements)
# Time Complexity: O(n)
# Space Complexity: O(n)