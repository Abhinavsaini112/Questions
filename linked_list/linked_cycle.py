from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers
        slow = head
        fast = head
        
        # Traverse the list with two pointers
        while fast is not None and fast.next is not None:
            slow = slow.next           # Move slow pointer by one step
            fast = fast.next.next      # Move fast pointer by two steps
            
            # If the two pointers meet, a cycle is detected
            if slow == fast:
                return True
        
        # If fast reaches the end, no cycle exists
        return False
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         curr=head
#         while curr is not None:
#             curr.val='x'
#             curr=curr.next
#             if curr is not None and curr.val=='x':
#                 return True
#         return False
        