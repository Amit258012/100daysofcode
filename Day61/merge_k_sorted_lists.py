# https://leetcode.com/problems/merge-k-sorted-lists/

"""
Time complexity:- O(N logK)
Space Complexity:- O(K) 
"""

"""
Intuition:

A min-heap (h) is used to keep track of the smallest element from each list. The heap is ordered based on the values of the nodes.
The algorithm initializes the min-heap with the first element from each list.
In each iteration, it pops the smallest element from the heap, adds it to the merged list, and pushes the next element from the same list to the heap if available.
This process continues until the min-heap is empty, resulting in a merged sorted list.
"""

import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a dummy head for the merged list.
        head = ListNode(None)
        # 'curr' will be used to traverse and build the merged list.
        curr = head
        # 'h' is a min-heap to keep track of the smallest element from each list.
        h = []

        # Initialize the min-heap with the first element from each list.
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        # Continue until the min-heap is not empty.
        while h:
            # Pop the smallest element from the min-heap.
            val, i = heapq.heappop(h)
            # Add the smallest element to the merged list.
            curr.next = ListNode(val)
            curr = curr.next
            # If there's another element in the same list, add it to the min-heap.
            if lists[i]:
                heapq.heappush(h, (lists[i].val, i))
                lists[i] = lists[i].next

        # Return the merged list starting from the second node (as the first is a dummy head).
        return head.next
