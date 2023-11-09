# https://leetcode.com/problems/find-k-closest-elements/

"""
Time complexity:- O(N logk)
Space Complexity:- O(K) 
"""

import heapq
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) < k:
            return []  # If the array size is less than k, return an empty list

        # Max heap to maintain the k elements with the maximum distance from x
        maxHeap = []

        for num in arr:
            # Calculate the distance between the current element and x
            dist = abs(num - x)

            if len(maxHeap) < k:
                # Push the negative distance to create a max heap
                heapq.heappush(maxHeap, (-dist, num))
            else:
                # If the distance is smaller than the maximum distance in the max heap, replace it
                if -1 * maxHeap[0][0] > dist:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap, (-dist, num))

        # Return the sorted list of k elements
        return sorted([val for _, val in maxHeap])
