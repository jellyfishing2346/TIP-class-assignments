class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mystery_function(head):
    nums1 = []  # To store even values (incorrectly named in the code's logic)
    nums2 = []  # To store odd values (incorrectly named in the code's logic)
    current = head
    while current:
        if current.val % 2 == 0:
            nums1.append(str(current.val))
        else:
            nums2.append(str(current.val))
        current = current.next
        
    return " -> ".join(nums2 + nums1)

# Create Linked List: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print(mystery_function(head)) # Expected Output: 1 -> 3 -> 5 -> 2 -> 4