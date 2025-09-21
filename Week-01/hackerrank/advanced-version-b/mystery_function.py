def mystery_function(s):
    sequence = "aeiouAEIOU"
    result = ""
    for char in s:
        if char not in sequence:
            result += char
    return result

result = mystery_function("CodePath")
print(result) # Output: CdPth