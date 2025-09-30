def mystery_function(word):
    result = {}
    for letter in word:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

word = "banana"
result = mystery_function(word)
print(result) # Output: {'b': 1, 'a': 3, 'n': 2}