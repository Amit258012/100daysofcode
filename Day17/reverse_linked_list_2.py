"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.
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
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Create a dummy node to simplify boundary cases
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head

        # Move leftPrev and cur to the left-1 and left-th nodes, respectively
        for i in range(left - 1):
            leftPrev = cur
            cur = cur.next

        prev = None
        for j in range(right - left + 1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext

        # Update the pointers to connect the reversed sub-section
        leftPrev.next.next = cur
        leftPrev.next = prev

        # Return the head of the modified linked list
        return dummy.next
