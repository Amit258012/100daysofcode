# https://leetcode.com/problems/find-missing-observations/

"""
Time complexity:- O(1) performs a fixed number of operations
Space Complexity:- O(1) 
"""


from typing import List


class Solution:
    def findRolls(self, rolls, mean, n):
        m = len(rolls)  # Get the number of available dice rolls
        curSum = sum(rolls)  # Calculate the current sum of dice rolls
        # Calculate the sum needed for the desired mean
        missingSum = mean * (n + m) - curSum

        # If the missing sum is not within the possible range, return an empty list
        if missingSum < n or missingSum > 6 * n:
            return []

        # Divide the missing sum into equal parts and remainder
        part, rem = divmod(missingSum, n)
        ans = [part] * n  # Initialize a list with equal parts

        # Distribute the remaining sum by incrementing values in the list
        for i in range(rem):
            ans[i] += 1

        return ans  # Return the list of dice roll values
