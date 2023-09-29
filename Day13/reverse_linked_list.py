"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for previous, current, and next elements
        prev_node = None
        current_node = head
        next_node = None

        while current_node:
            # Save the next node for iteration
            next_node = current_node.next

            # Reverse the direction of the current node's pointer
            current_node.next = prev_node

            # Move the pointers forward for the next iteration
            prev_node = current_node
            current_node = next_node

        # The reversed list starts with the previous node
        return prev_node
