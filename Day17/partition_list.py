"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
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
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Create two dummy nodes for the left and right partitions
        left, right = ListNode(), ListNode()
        lTail, rTail = left, right

        while head:
            if head.val < x:
                # Append the current node to the left partition
                lTail.next = head
                lTail = lTail.next
            else:
                # Append the current node to the right partition
                rTail.next = head
                rTail = rTail.next
            head = head.next

        # Connect the tail of the left partition to the head of the right partition
        lTail.next = right.next

        # Set the tail of the right partition to None (to terminate the list)
        rTail.next = None

        # Return the head of the modified linked list with partitions
        return left.next
