# https://leetcode.com/problems/longest-increasing-subsequence/
"""
Time complexity:- O(N^2)
Space Complexity:- O(N) 
"""

"""
Intuition:

The lengthOfLIS function uses dynamic programming to find the length of the longest increasing subsequence (LIS) in the given array.
It iterates through the array in reverse, comparing elements to find the LIS.
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize an array to store the length of the longest increasing subsequence ending at each index.
        LIS = [1] * len(nums)

        # Iterate through the array in reverse.
        for i in range(len(nums) - 1, -1, -1):
            # For each index i, iterate through the elements to its right (j > i).
            for j in range(i + 1, len(nums)):
                # If the element at index i is less than the element at index j,
                # update the length of LIS ending at i based on LIS ending at j.
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        # Return the maximum length of LIS.
        return max(LIS)
