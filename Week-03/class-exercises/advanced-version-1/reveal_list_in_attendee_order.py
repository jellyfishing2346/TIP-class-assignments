def reveal_attendee_list_in_order(attendees):
    from collections import deque
    
    # Sort attendees to get the desired reveal order
    sorted_attendees = sorted(attendees)
    
    # Use deque to simulate the queue
    queue = deque()
    
    # Work backwards from the sorted order
    for attendee in reversed(sorted_attendees):
        # If queue is not empty, move the last person to front (reverse of moving front to back)
        if queue:
            queue.appendleft(queue.pop())
        
        # Add current attendee to the front
        queue.appendleft(attendee)
    
    return list(queue)

# Test the function
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7]))  # Expected: [2,13,3,11,5,17,7]
print(reveal_attendee_list_in_order([1,1000]))           # Expected: [1,1000]
