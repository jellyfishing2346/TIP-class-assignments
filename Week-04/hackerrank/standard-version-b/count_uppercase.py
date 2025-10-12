def count_uppercase(my_string):
    count = 0
    for char in my_string:
        if char.isupper():
            count += 1
    return count # Time complexity: O(n)