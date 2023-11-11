# https://leetcode.com/problems/last-stone-weight/

"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Create a max heap (negate each element to simulate a min heap)
        h = [-x for x in stones]
        heapq.heapify(h)

        # Continue the process until only one or no stone is left
        while len(h) > 1 and h[0] != 0:
            # Pop the two largest stones from the max heap
            stone1 = heapq.heappop(h)
            stone2 = heapq.heappop(h)

            # Calculate the weight difference and push it back into the max heap
            diff = stone1 - stone2
            heapq.heappush(h, diff)

        # If there is at least one stone remaining, return its weight
        return -h[0]
