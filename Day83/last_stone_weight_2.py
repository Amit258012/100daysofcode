# https://leetcode.com/problems/last-stone-weight-ii/
"""
Time complexity:- O(2^N)
Space Complexity:- O(N)
"""

"""
Intuition:

The code aims to find the minimum absolute difference between two groups of stones by exploring all possible combinations using a recursive approach.
Memoization is used to avoid redundant calculations and improve the efficiency of the algorithm.
The target value is calculated based on the sum of all stones, and the algorithm tries to minimize the difference between the two groups.
"""
from math import ceil
from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # Calculate the total sum of stones and the target value
        stoneSum = sum(stones)
        target = ceil(stoneSum / 2)

        # Define a recursive function to explore all possible combinations
        def dfs(i, total):
            # Base cases: if the total exceeds the target or all stones are considered
            if total >= target or i == len(stones):
                # Return the absolute difference between the current total and the remaining stones
                return abs(total - (stoneSum - total))

            # Check if the result for the current state is already calculated
            if (i, total) in dp:
                return dp[(i, total)]

            # Recursive case: explore both possibilities (take or skip the current stone)
            dp[(i, total)] = min(dfs(i + 1, total), dfs(i + 1, total + stones[i]))
            return dp[(i, total)]

        # Initialize a dictionary to store previously calculated results
        dp = {}

        # Return the result of the recursive function starting from the first stone and total = 0
        return dfs(0, 0)
