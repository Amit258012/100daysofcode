# https://leetcode.com/problems/combinations/

"""
Time complexity:- O(C(n,k))
Space Complexity:- O(C(n,k))
"""
from types import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []  # Initialize a list to store the resulting combinations.

        def backtrack(start, comb):
            # If the combination size matches 'k', add it to the result.
            if len(comb) == k:
                res.append(comb[:])
                return

            for i in range(start, n + 1):
                comb.append(i)  # Add the current integer to the combination.
                backtrack(i + 1, comb)  # Recursively generate combinations.
                comb.pop()  # Remove the last element to backtrack.

        # Start the backtracking process with an initial value of '1'.
        backtrack(1, [])

        return res  # Return the list of generated combinations.
