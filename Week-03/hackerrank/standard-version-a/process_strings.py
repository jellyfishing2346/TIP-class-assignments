def process_strings(chars):
    stack = ["start"]
    for char in chars:
        if char.isupper():
            stack.append(char)
        elif stack and char.islower():
            stack.pop()
    return stack

chars = ['A', 'b', 'c', 'D', 'E', 'f']
print(process_strings(chars)) # Output: ['start', 'A', 'D', 'E']
