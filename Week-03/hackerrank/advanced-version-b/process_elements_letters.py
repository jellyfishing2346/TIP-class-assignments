from collections import deque

def process_elements(elements):
    queue = deque()
    stack = []
    for element in elements:
        queue.append(element)
    while queue:
        item = queue.popleft()
        stack.append(item)
        if len(stack) % 2 == 0 and queue:
            stack.pop()
    return list(stack)

# Test case
result = process_elements(["a", "b", "c", "d", "e"])
print(result)
