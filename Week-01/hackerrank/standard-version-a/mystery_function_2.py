def mystery_function(lst, threshold):
    total = 0
    i = 0
    while i < len(lst) and total <= threshold:
        total += lst[i]
        i += 1
    return total

result = mystery_function([1, 2, 3, 4, 5], 7)
print(result)
# Output: 10