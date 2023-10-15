# https://leetcode.com/problems/permutations/

"""
Time complexity:- O(n!)
Space Complexity:- O(n!)
"""
from types import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Base case: If there's only one element, return a list with that element.
        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)  # Remove the first element from the list.

            # Recursively compute permutations for the remaining elements.
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)  # Add the removed element to each permutation.

            res.extend(perms)  # Extend the result list with the computed permutations.

            # Restore the removed element to its original position in the list.
            nums.append(n)
        return res  # Return the list of all permutations.
