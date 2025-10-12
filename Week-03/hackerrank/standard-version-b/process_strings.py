from collections import deque

def process_strings(chars):
    queue = deque(["start", "middle", "end"])
    for char in chars:
        if char.isupper():
            queue.append(char)
        elif queue and char.islower():
            queue.popleft()
    return list(queue)

chars = ['A', 'b', 'C', 'd', 'E', 'f']
print(process_strings(chars)) # Output: ['A', 'C', 'E']