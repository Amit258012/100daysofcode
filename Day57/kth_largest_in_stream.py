# https://leetcode.com/problems/kth-largest-element-in-a-stream/

"""
Time complexity:- O(N logk)
Space Complexity:- O(K) 
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums  # Initialize the min-heap with the initial elements
        self.k = k  # Set the value of k
        heapq.heapify(self.minHeap)  # Convert the list into a min-heap
        while len(self.minHeap) > k:
            # If the heap size exceeds k, pop the minimum element
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)  # Push the new value onto the min-heap
        if len(self.minHeap) > self.k:
            # If the heap size exceeds k, pop the minimum element
            heapq.heappop(self.minHeap)
        return self.minHeap[0]  # The top element of the heap is the kth largest value


# Time Complexity (TC):
# - Initialization: O(N * log(k)), where N is the number of initial elements.
# - Adding an element: O(log(k)).
# - Removing an element: O(log(k)).
# - Heapify an array: O(N).
