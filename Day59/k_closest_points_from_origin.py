# https://leetcode.com/problems/k-closest-points-to-origin/

"""
Time complexity:- O(N logK)
Space Complexity:- O(K) 
"""

import heapq
from typing import List


class Solution:
    # Function to calculate the distance from the origin (0, 0)
    def distance(self, x: int, y: int) -> int:
        return x**2 + y**2

    # Function to find the k closest points to the origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []  # Max heap to store points along with their negative distances
        res = []  # Result array to store the k closest points

        # Iterate through the points
        for x, y in points:
            dist = self.distance(x, y)
            # Push the point and its negative distance into the max heap
            heapq.heappush(maxHeap, (-dist, [x, y]))

            # If the heap size exceeds k, pop the point with the maximum distance
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        # Pop points from the max heap to get the k closest points
        while maxHeap:
            _, points = heapq.heappop(maxHeap)
            res.append(points)

        return res
