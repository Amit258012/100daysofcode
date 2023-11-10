# https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/0

"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

import heapq
from typing import List


class Solution:
    # Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr: List[int]) -> int:
        minHeap = []  # Min heap to store the lengths of the ropes
        totalCost = 0  # Variable to store the total cost of connecting the ropes

        # Push the lengths of the ropes into the min heap
        for num in arr:
            heapq.heappush(minHeap, num)

        # Continue connecting ropes until only one rope is left
        while len(minHeap) > 1:
            # Pop the two smallest ropes from the min heap
            minVal1 = heapq.heappop(minHeap)
            minVal2 = heapq.heappop(minHeap)

            # Calculate the cost of connecting these two ropes
            curCost = minVal1 + minVal2

            # Add the cost to the total cost
            totalCost += curCost

            # Push the connected rope back into the min heap
            heapq.heappush(minHeap, curCost)

        return totalCost
