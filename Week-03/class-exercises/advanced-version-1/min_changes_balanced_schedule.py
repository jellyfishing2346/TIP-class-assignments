def min_changes_to_make_balanced(schedule):
    open_count = 0
    unmatched_close = 0
    
    for char in schedule:
        if char == '(':
            open_count += 1
        elif char == ')':
            if open_count > 0:
                open_count -= 1  # Match with a previous opening
            else:
                unmatched_close += 1  # No opening to match with
    
    # open_count = unmatched opening parentheses that need closing
    # unmatched_close = unmatched closing parentheses that need opening
    return open_count + unmatched_close

# Test the function
print(min_changes_to_make_balanced("())"))  # Expected: 1
print(min_changes_to_make_balanced("((("))  # Expected: 3
