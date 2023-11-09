# https://leetcode.com/problems/top-k-frequent-elements/

"""
Time complexity:- O(N logk)
Space Complexity:- O(K) 
"""

import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}  # Dictionary to store the frequency of each number

        # Count the frequency of each number in the input list
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)

        maxHeap = []  # Max heap to maintain the k elements with the highest frequency

        # Push the elements along with their negative frequencies to create a max heap
        for val, freq in hmap.items():
            heapq.heappush(maxHeap, (-freq, val))

        res = []

        # Pop the k elements with the highest frequency from the max heap
        for _ in range(k):
            res.append(heapq.heappop(maxHeap)[1])

        return res
