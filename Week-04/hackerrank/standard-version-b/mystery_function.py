def mystery_function(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]

d = {'a': [1, 2], 'b': [3, 4]}
mystery_function(d, 'a', 5)
mystery_function(d, 'c', 6)
print(d) # Output: {'a': [1, 2, 5], 'b': [3, 4], 'c': [6]}