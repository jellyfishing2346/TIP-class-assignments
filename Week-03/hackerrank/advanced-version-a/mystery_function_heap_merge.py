import heapq

def mystery_function(lists):
    min_heap = []
    # Initialize the heap with the first element of each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    result_list = []
    # Extract-min and push the next element from the same list
    while min_heap:
        value, list_idx, element_idx = heapq.heappop(min_heap)
        result_list.append(value)
        next_idx = element_idx + 1
        if next_idx < len(lists[list_idx]):
            heapq.heappush(min_heap, (lists[list_idx][next_idx], list_idx, next_idx))
    return result_list

# Test case
result = mystery_function([[1, 3], [2, 4]])
print(result)
