# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

"""
Time complexity:- O(N logN)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code sorts the pairs based on the second element (tail) in ascending order.
It iterates through the sorted pairs, selecting pairs such that the head is greater than the current tail.
The length of the longest chain is updated accordingly.
"""
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # Sort the array in ascending order.
        arr.sort()

        # Initialize the answer to 1.
        max_element = 1

        # Iterate through the sorted array.
        for i in range(1, len(arr)):
            # If the current element is greater than or equal to the answer + 1,
            # update the answer by incrementing it.
            if arr[i] >= max_element + 1:
                max_element += 1

        # Return the maximum element after decrementing and rearranging.
        return max_element
