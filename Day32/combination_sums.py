# https://leetcode.com/problems/combination-sum/

"""
Time complexity:- O(2^n)
Space Complexity:- O(2^n)
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # List to store the result

        def dfs(i, cur, total):
            if total == target:  # If the current combination sums up to the target
                res.append(cur.copy())  # Add a copy of the combination to the result
                return

            # If we've gone through all candidates or exceeded the target
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate in the combination
            cur.append(candidates[i])
            # Recursively explore combinations with the current candidate
            dfs(i, cur, total + candidates[i])

            # Remove the current candidate (backtrack)
            cur.pop()
            # Recursively explore combinations without the current candidate

            dfs(i + 1, cur, total)

        dfs(0, [], 0)  # Start the DFS with the initial values

        return res  # Return the list of combinations that sum up to the target
