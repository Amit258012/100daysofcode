"""
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to simplify boundary cases
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur:
            # Check for duplicates in the current sequence
            while cur.next and cur.next.val == cur.val:
                cur = cur.next

            # If there are no duplicates, move both prev and cur pointers
            if prev.next == cur:
                prev = prev.next
                cur = cur.next
            else:
                # Update the pointers to skip the duplicates
                prev.next = cur.next
                cur = prev.next

        # Return the head of the modified linked list (without duplicates)
        return dummy.next
