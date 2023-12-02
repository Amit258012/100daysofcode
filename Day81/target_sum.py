# https://leetcode.com/problems/target-sum/
"""
Time complexity:- O(2^N)
Space Complexity:- O(N)
"""

"""
Intuition:

The code addresses the problem of finding the number of ways to reach a target sum by assigning either a positive or negative sign to each element in the array.
Backtracking is used to explore all possible combinations, and memoization is employed to avoid redundant calculations and improve efficiency.
The recursive function ('backtrack') calculates the number of ways by considering two possibilities at each step: adding the current element or subtracting it.
The final result is the number of ways to reach the target sum starting from the first element of the array with an initial total of 0.
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Dictionary to memoize results of subproblems: (index, total) -> # of ways
        dp = {}

        # Backtracking function to explore all possible combinations
        def backtrack(i, total):
            # Base case: if we have processed all elements in the array
            if i == len(nums):
                # Return 1 if the total matches the target, otherwise 0
                return 1 if total == target else 0

            # Check if the result for the current subproblem is already memoized
            if (i, total) in dp:
                return dp[(i, total)]

            # Recursively calculate the number of ways by considering two possibilities:
            # 1. Adding the current element
            # 2. Subtracting the current element
            dp[(i, total)] = backtrack(i + 1, total + nums[i]) + backtrack(
                i + 1, total - nums[i]
            )

            # Return the result for the current subproblem
            return dp[(i, total)]

        # Start the backtracking process from the first element with an initial total of 0
        return backtrack(0, 0)
