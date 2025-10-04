def mystery_function(words):
    result = {}
    for word in words:
        initial = word[0]
        if initial not in result:
            result[initial] = []
        result[initial].append(word)
    return result
words = ["apple", "banana", "apple", "cherry", "apricot", "blueberry", "avocado"]
print(mystery_function(words))
# Output: {'a': ['apple', 'apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}