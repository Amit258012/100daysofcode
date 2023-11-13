# https://leetcode.com/problems/maximum-sum-circular-subarray/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code uses Kadane's algorithm to find the maximum and minimum subarray sums for a non-circular array.
It simultaneously calculates the total sum of the array.
The maximum circular subarray sum can be either the maximum non-circular subarray sum (globMax) or the sum of the remaining circular subarray (total - globMin).
If globMax is non-positive, the array consists of all negative values, so the maximum circular subarray sum is equal to globMax.
"""

from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Initialize variables to track global maximum, global minimum,
        # current maximum, current minimum, and the total sum.
        globMax, globMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        # Iterate through the array to find the maximum circular subarray sum.
        for i, n in enumerate(nums):
            # Update current maximum and minimum for non-circular subarray.
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            # Calculate the total sum of the array.
            total += n
            # Update global maximum and minimum for the circular subarray.
            globMax = max(curMax, globMax)
            globMin = min(curMin, globMin)

        # Return the maximum of global maximum and (total sum - global minimum),
        # unless global maximum is non-positive, then return global maximum.
        return max(globMax, total - globMin) if globMax > 0 else globMax
