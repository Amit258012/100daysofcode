"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
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
    def getKth(self, cur, k):
        # Helper function to get the k-th node from the current node
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Create a dummy node to simplify boundary cases
        dummy = ListNode(0, head)
        grpPrev = dummy

        while True:
            # Find the k-th node from the current group
            kth = self.getKth(grpPrev, k)

            # If there are fewer than k nodes left, break the loop
            if not kth:
                break

            # Get the next group's head
            grpNext = kth.next

            # Reverse the current group
            prev, cur = kth.next, grpPrev.next
            while cur != grpNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            # Connect the reversed group to the previous group (or the dummy node)
            temp = grpPrev.next
            grpPrev.next = kth
            grpPrev = temp

        # Return the head of the modified linked list
        return dummy.next
