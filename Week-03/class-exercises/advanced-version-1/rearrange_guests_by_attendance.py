def rearrange_guests(guests):
    # Separate positive and negative numbers while preserving order
    positive = [num for num in guests if num > 0]
    negative = [num for num in guests if num < 0]
    
    result = []
    
    # Alternate between positive and negative, starting with positive
    for i in range(len(positive)):
        result.append(positive[i])
        if i < len(negative):
            result.append(negative[i])
    
    return result

# Test the function
print(rearrange_guests([3,1,-2,-5,2,-4]))  # Expected: [3,-2,1,-5,2,-4]
print(rearrange_guests([-1,1]))            # Expected: [1,-1]
