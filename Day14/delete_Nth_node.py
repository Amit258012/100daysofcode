"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""

from typing import ListNode, Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize two pointers, fast and slow
        fast = head
        slow = head

        # Move the fast pointer n nodes ahead
        for i in range(n):
            fast = fast.next

        # If fast has reached the end, remove the head node
        if not fast:
            return head.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Skip the nth node by updating the next pointer of the previous node
        slow.next = slow.next.next

        # Return the modified linked list
        return head
