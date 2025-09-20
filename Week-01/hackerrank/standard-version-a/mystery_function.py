def mystery_function(s):
    count = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
    return count

result = mystery_function("AABBAB")
print(result)
# Output: 2