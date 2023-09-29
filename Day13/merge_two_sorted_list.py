"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Base cases: if one of the lists is empty, return the other list
        if not l1:
            return l2
        if not l2:
            return l1
        # Compare the values of the current nodes in l1 and l2
        elif l1.val <= l2.val:
            # If l1's value is smaller, set l1's next to the merged list of l1's next and l2
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            # If l2's value is smaller, set l2's next to the merged list of l1 and l2's next
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
