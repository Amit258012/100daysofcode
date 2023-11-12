# https://leetcode.com/problems/find-median-from-data-stream/

"""
Time Complexity:
    __init__: O(1)
    addNum: O(log n)
    findMedian: O(1)
    
Space Complexity:
    O(n)
"""

"""
Intuition:

The addNum method inserts a number into either the large (min heap) or small (max heap) heap, maintaining the property that large[0] is greater than or equal to all elements in small.
The heaps are balanced so that the size difference between them is at most 1. This ensures that the median can be found efficiently.
The findMedian method calculates and returns the median based on the sizes of the heaps. If the heaps have equal size, the average of the top elements is returned; otherwise, the top element of the larger heap is returned.
"""

import heapq


class MedianFinder:
    def __init__(self):
        # Two heaps to maintain the stream of numbers
        # large: Min heap to store larger half of the numbers
        # small: Max heap to store smaller half of the numbers (negated for max heap effect)
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        # Add the number to the appropriate heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Balance the heaps so that the size difference is at most 1
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    def findMedian(self) -> float:
        # Calculate and return the median based on the sizes of the heaps
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2.0
