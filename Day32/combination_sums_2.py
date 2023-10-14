# https://leetcode.com/problems/combination-sum/

"""
Time complexity:- O(2^n)
Space Complexity:- O(2^n)
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []  # List to store the result
        candidates.sort()  # Sort the candidates list to easily skip duplicates

        def dfs(idx, path, cur):
            if cur > target:
                return  # Stop exploring if the current sum exceeds the target

            # If the current sum equals the target, add the combination to the result
            if cur == target:
                res.append(path)
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates to avoid duplicate combinations

                # Explore combinations with the current candidate
                dfs(i + 1, path + [candidates[i]], cur + candidates[i])

        dfs(0, [], 0)  # Start the depth-first search (DFS) from the first candidate
        return res  # Return the list of unique combinations that sum up to the target
