"""
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
"""
"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # Handle edge cases for arrays of size 1 and 2.
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        # Initialize left and right pointers.
        l = 1
        h = n - 2

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                # If the element is greater than its neighbors, it's a peak.
                return mid

            if nums[mid] > nums[mid - 1]:
                l = mid + 1
            else:
                h = mid - 1

        return -1
