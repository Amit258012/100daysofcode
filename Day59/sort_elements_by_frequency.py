# https://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency-1587115621/1

"""
Time complexity:- O(N logN)
Space Complexity:- O(N) 
"""

import heapq
from collections import Counter
from typing import List


class Solution:
    def sortByFreq(self, a: List[int]) -> List[int]:
        maxHeap = []  # Max heap to store elements along with their negative frequencies
        res = []  # Result array to store the sorted elements

        # Count the frequency of each element using Counter
        d = Counter(a)

        # Push elements into max heap with their negative frequencies
        for num in a:
            heapq.heappush(maxHeap, (-d[num], num))

        # Pop elements from max heap to get the sorted array
        while maxHeap:
            _, val = heapq.heappop(maxHeap)
            res.append(val)

        return res


# Time Complexity (TC):
# - Constructing the max-heap: O(n * log(n))
# - Popping from the max-heap: O(n * log(n))
# - Overall: O(n * log(n))

# Space Complexity (SC):
# - O(n) for the Counter dictionary.
# - O(n) for the max-heap.
