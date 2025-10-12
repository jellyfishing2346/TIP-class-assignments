import heapq

def mystery_function(nums, k):
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    return min_heap[0]

# Test case
result = mystery_function([3, 2, 1, 5, 6, 4], 2)
print(result)
