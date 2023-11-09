# https://practice.geeksforgeeks.org/problems/nearly-sorted-1587115620/1

"""
Time complexity:- O(N logk)
Space Complexity:- O(K) 
"""

import heapq


class Solution:
    def nearlySorted(self, arr, k):
        res = []  # Result array to store the nearly sorted elements
        minHeap = []  # Min heap to maintain the k-sized sliding window

        for num in arr:
            heapq.heappush(minHeap, num)  # Push the current element into the min-heap

            if len(minHeap) > k:
                # Pop the minimum element if the window size exceeds k
                res.append(heapq.heappop(minHeap))

        # Process any remaining elements in the min-heap
        while minHeap:
            res.append(heapq.heappop(minHeap))

        return res
