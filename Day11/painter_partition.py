"""
Split array largest sum or painter partition
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Time Complexity:- O(N * log(sum(arr[])-max(arr[])+1))
Space Complexity:- o(1)
"""

from typing import List


class Solution:
    def paint(self, nums, p):
        n = len(nums)
        painters = 1
        max_unit = 0

        for i in range(n):
            if max_unit + nums[i] <= p:
                max_unit += nums[i]
            else:
                painters += 1
                max_unit = nums[i]
        return painters

    def painterPartition(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k > n:
            return (
                -1
            )  # If the number of subarrays to split is greater than the number of elements, it's not possible.

        l = max(
            nums
        )  # Minimum possible largest sum is the maximum unit of a single board.
        h = sum(nums)  # Maximum possible largest sum is the sum of all board units.

        while l <= h:
            mid = (l + h) // 2
            painters = self.paint(nums, mid)

            if painters > k:
                l = mid + 1
            else:
                h = mid - 1

        return l  # Return the minimized largest sum of the split.
