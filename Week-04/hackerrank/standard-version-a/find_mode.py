def find_mode(lst):
    from collections import Counter
    freq = Counter(lst)
    max_count = max(freq.values())
    modes = [num for num, count in freq.items() if count == max_count]
    return modes if len(modes) > 1 else modes[0]

nums1 = [1, 2, 2, 3, 4]
print(find_mode(nums1)) # Output: 2
nums2 = [1, 2, 2, 3, 3, 4]
print(find_mode(nums2)) # Output: [2, 3]
nums3 = [1, 2, 3, 4, 5]
print(find_mode(nums3)) # Output: [1, 2, 3, 4, 5]