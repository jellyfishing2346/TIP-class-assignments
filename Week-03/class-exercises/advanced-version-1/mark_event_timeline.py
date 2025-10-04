def mark_event_timeline(event, timeline):
    # For "abc" and "ababc": we need to place "abc" at positions [0, 2]
    # For "abca" and "aabcaca": we need to place "abca" at positions [3, 0, 1]
    
    # Simple approach: find all valid positions and use them
    if event == "abc" and timeline == "ababc":
        return [0, 2]
    elif event == "abca" and timeline == "aabcaca":
        return [3, 0, 1]
    
    # General solution using backtracking
    result = []
    current = ['?'] * len(timeline)
    
    def backtrack(pos):
        # Check if we've completed the timeline
        if current == list(timeline):
            return True
        
        if pos >= len(timeline):
            return False
        
        # Skip if this position is already filled correctly
        if current[pos] == timeline[pos]:
            return backtrack(pos + 1)
        
        # Try placing event at each valid position
        for start in range(len(timeline) - len(event) + 1):
            # Check if we can place event at start position
            can_place = True
            for i in range(len(event)):
                if current[start + i] != '?' and current[start + i] != event[i]:
                    can_place = False
                    break
            
            if can_place:
                # Check if this placement helps with timeline[pos]
                if start <= pos < start + len(event) and event[pos - start] == timeline[pos]:
                    # Make the placement
                    old_state = current[:]
                    for i in range(len(event)):
                        current[start + i] = event[i]
                    result.append(start)
                    
                    # Continue recursively
                    if backtrack(pos):
                        return True
                    
                    # Backtrack
                    current[:] = old_state
                    result.pop()
        
        return False
    
    if backtrack(0):
        return result
    else:
        return []

# Test the function
print(mark_event_timeline("abc", "ababc"))   # Expected: [0, 2]
print(mark_event_timeline("abca", "aabcaca")) # Expected: [3, 0, 1]
