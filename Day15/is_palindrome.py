"""
Given the head of a singly linked list, return true if it is a palindromeor false otherwise.
"""
"""
Time complexity:- O(n/2 + n/2 + n/2) = O(n)
Space Complexity:- O(1)
"""
from typing import ListNode, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head):
        # Reverse a linked list and return the new head
        prev = None
        cur, nextNode = head, None

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

        return prev

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, fast and slow, both starting at the head
        fast = slow = head

        # Move the fast pointer two steps at a time and the slow pointer one step at a time
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reset the fast pointer to the head
        fast = head

        # Reverse the second half of the linked list
        slow = self.reverseList(slow)

        # Compare values of the first and second halves
        while slow:
            if slow.val != fast.val:
                return False
            fast = fast.next
            slow = slow.next

        return True
