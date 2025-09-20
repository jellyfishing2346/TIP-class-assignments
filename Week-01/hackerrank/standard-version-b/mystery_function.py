def mystery_function(s, specific_digits):
    count = 0
    for char in s:
        if char in specific_digits:
            count += 1
    return count

result = mystery_function("There are 2 apples, 3 bananas, 5 cherries, and 7 dates.", "2378")
print(result)  # Output: 3