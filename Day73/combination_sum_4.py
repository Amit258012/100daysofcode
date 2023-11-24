# https://leetcode.com/problems/combination-sum-iv/
"""
Time complexity:- O(target * N)
Space Complexity:- O(target) 
"""

"""
Intuition:

Subproblems are solved in a bottom-up manner, iteratively computing the count of combinations for each total from 1 to the target. The accumulation of counts is efficiently performed by considering both inclusion and exclusion of each element from the given nums array.
"""


from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Using dynamic programming to solve the problem

        # Initialize a cache to store intermediate results
        cache = {0: 1}

        # Build up the cache for each total from 1 to target
        for total in range(1, target + 1):
            cache[total] = 0
            # Iterate through the given numbers
            for n in nums:
                # Accumulate the count by adding the count for (total - n)
                cache[total] += cache.get(total - n, 0)

        # The result is the count for the target
        return cache[target]
