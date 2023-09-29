"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
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
    def hasCycle(self, head):
        # Initialize both slow and fast pointers to the head of the linked list
        slow = fast = head

        # Traverse the list with two pointers
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            # If there's a cycle, the fast pointer will eventually catch up to the slow pointer
            if fast == slow:
                return slow

        # If there's no cycle, return None
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize an entry pointer to the head of the linked list
        entry = head

        # Find the node where the slow and fast pointers meet (if there's a cycle)
        slow = self.hasCycle(head)

        # If there's no cycle, return None
        if not slow:
            return None

        # Move the entry pointer and the slow pointer until they meet at the start of the cycle
        while entry:
            if slow == entry:
                return entry
            entry = entry.next
            slow = slow.next

        # Return the starting node of the cycle
        return None
