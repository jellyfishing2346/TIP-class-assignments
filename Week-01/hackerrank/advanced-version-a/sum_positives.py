def sum_positives(lst):
    total = 0
    for num in lst:
        if num > 0:
            total += num
    return total

result = sum_positives([-1, 2, 3, 4, -5])
print(result)  # Output: 9