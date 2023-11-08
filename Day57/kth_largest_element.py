# https://leetcode.com/problems/kth-largest-element-in-an-array/

"""
Time complexity:- O(N logk)
Space Complexity:- O(K) 
"""

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []  # Initialize a min-heap
        for num in nums:
            heapq.heappush(pq, num)  # Push elements onto the min-heap

            if len(pq) > k:
                heapq.heappop(pq)  # If the heap size exceeds k, pop the minimum element

        return pq[0]  # The top element of the heap is the kth largest value
