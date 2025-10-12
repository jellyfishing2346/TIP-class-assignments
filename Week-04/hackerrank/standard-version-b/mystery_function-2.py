from collections import deque

def mystery_function(lst):
    queue = deque(lst)
    output = []
    while queue:
        output.append(queue.pop())
    
    return "".join(output)
result = mystery_function(["h", "e", "l", "l", "o"]) # "olleh"
print(result)