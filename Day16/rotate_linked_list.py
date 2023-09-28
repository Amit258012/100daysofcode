"""
Given the head of a linked list, rotate the list to the right by k places.
"""
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import ListNode, Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base case: If the linked list is empty or has only one node, return it as is
        if head is None or head.next is None:
            return head

        # Calculate the length of the linked list
        cur = head
        count = 0
        while cur and cur.next:
            count += 1
            cur = cur.next
        count += 1

        # Calculate the effective rotation count
        k = k % count

        # If k is 0, the list remains the same, so return the original head
        if k == 0:
            return head

        # Initialize fast and slow pointers
        fast = head
        slow = head

        # Move the fast pointer k nodes ahead
        for i in range(k):
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Update the new head of the rotated list
        newHead = slow.next
        slow.next = None

        # Connect the end of the rotated list to the original head
        temp = newHead
        while newHead and newHead.next:
            newHead = newHead.next
        newHead.next = head

        # Return the new head of the rotated list
        return temp
