"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
"""
"""
Time complexity:- O(2 max(n,m))
Space Complexity:- O(1)
"""


class Solution:
    def getIntersectionNode(self, headA, headB):
        # Initialize two pointers, dummy1 and dummy2, to the heads of the input linked lists
        dummy1 = headA
        dummy2 = headB

        # Traverse both linked lists until they either intersect or reach the end (None)
        while dummy1 != dummy2:
            # If either of the pointers reaches the end of its list, move it to the other list's head
            if dummy1 is None:
                dummy1 = headB
            if dummy2 is None:
                dummy2 = headA

            # Move both pointers one step forward
            dummy1 = dummy1.next
            dummy2 = dummy2.next

        # Return either the intersection node or None if there is no intersection
        return dummy1
