"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
"""
Time complexity:- O(max(n,m))
Space Complexity:- O(1)
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Create a dummy head and a tail pointer for the result linked list
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0  # Initialize the carry to 0

        while l1 or l2 or carry != 0:
            # Get the current digits of l1 and l2 (or 0 if one of them is None)
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # Calculate the sum of the digits and the carry
            _sum = digit1 + digit2 + carry
            digit = _sum % 10
            carry = _sum // 10

            # Create a new node with the calculated digit
            newNode = ListNode(digit)

            # Append the new node to the result linked list
            tail.next = newNode
            tail = tail.next

            # Move to the next nodes in l1 and l2 (if available)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Get the result linked list starting from the node after the dummy head
        result = dummyHead.next

        # Remove the reference to the rest of the linked list
        dummyHead.next = None

        return result  # Return the result linked list
