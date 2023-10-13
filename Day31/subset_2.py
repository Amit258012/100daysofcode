# https://leetcode.com/problems/subsets-ii
"""
Time complexity:- O(2^n)
Space Complexity:- O(n)
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []  # List to store the subsets
        subset = []  # List to track the current subset during DFS
        nums.sort()  # Sort the input list to handle duplicates

        def dfs(i, subset):
            if i >= len(nums):
                # Add a copy of the current subset to the result
                res.append(subset.copy())
                return

            # Include the element at index i (left tree)
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude the element at index i (right tree)
            dfs(i + 1, subset)

        dfs(0, subset)  # Start DFS from index 0
        return res
