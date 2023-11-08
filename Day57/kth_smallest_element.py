# https://www.geeksforgeeks.org/problems/kth-smallest-element5635/1

"""
Time complexity:- O(N logk)
Space Complexity:- O(K) 
"""

import heapq


class Solution:
    def kthSmallest(self, arr, k):
        pq = []  # Initialize a max-heap (implemented as a min-heap with negated values)

        for num in arr:
            heapq.heappush(pq, -num)  # Negate the values and push them onto the heap

            if len(pq) > k:
                heapq.heappop(pq)  # If the heap size exceeds k, pop the maximum element

        return -pq[0]  # The top element of the heap (negated) is the kth smallest value
