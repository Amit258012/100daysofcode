"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""

from typing import ListNoteBook, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNoteBook]:
        # Initialize two pointers, cur and temp
        temp = head
        cur = head

        # Traverse the list with two pointers:
        # - cur moves one step at a time
        # - temp moves two steps at a time
        while temp and temp.next:
            cur = cur.next
            temp = temp.next.next

        # When temp reaches the end, cur will be at the middle
        return cur
