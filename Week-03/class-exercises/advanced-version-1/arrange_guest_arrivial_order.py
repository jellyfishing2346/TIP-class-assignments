def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    result = []
    stack = []
    
    for i in range(n + 1):
        stack.append(str(i + 1))
        
        # If we're at the end or the current pattern is 'I', pop from stack
        if i == n or arrival_pattern[i] == 'I':
            while stack:
                result.append(stack.pop())
    
    return ''.join(result)

# Test the function
print(arrange_guest_arrival_order("IIIDIDDD"))  # Expected: 123549876
print(arrange_guest_arrival_order("DDD"))       # Expected: 4321
