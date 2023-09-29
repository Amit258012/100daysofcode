"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
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
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize both pointers to the head of the linked list
        fast = head
        slow = head

        # Traverse the list with two pointers
        while fast and fast.next:
            # Move the fast pointer two steps at a time
            fast = fast.next.next
            # Move the slow pointer one step at a time
            slow = slow.next

            # If there's a cycle, the fast pointer will eventually catch up to the slow pointer
            if fast == slow:
                return True

        # If there's no cycle and the fast pointer reaches the end, return False
        return False
