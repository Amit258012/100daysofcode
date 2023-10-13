# https://leetcode.com/problems/subsets/
"""
Time complexity:- O(2^n)
Space Complexity:- O(n)
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []  # List to store the subsets
        subSet = []  # List to track the current subset during DFS

        def dfs(i):
            if i >= len(nums):
                # Add a copy of the current subset to the result
                res.append(subSet.copy())
                return

            # Take the element at index i (left tree)
            subSet.append(nums[i])
            dfs(i + 1)

            # Leave the element at index i (right tree)
            subSet.pop()
            dfs(i + 1)

        dfs(0)  # Start DFS from index 0
        return res
