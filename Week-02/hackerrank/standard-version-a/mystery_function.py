def mystery_function(old_dictionary):
    new_dictionary = {}
    for key, value in old_dictionary.items():
        if value not in new_dictionary:
            new_dictionary[value] = [key]
        else:
            new_dictionary[value].append(key)
    return new_dictionary

old_dictionary = {'a': 1, 'b': 2, 'c': 1}
new_dictionary = mystery_function(old_dictionary)
print(new_dictionary)  # Output: {1: ['a', 'c'], 2: ['b']}