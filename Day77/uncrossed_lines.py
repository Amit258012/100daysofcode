# https://leetcode.com/problems/uncrossed-lines/
"""
Time complexity:- O(n1*n2)
Space Complexity:- O(n2) 
"""

"""
Intuition:

The code addresses the problem of finding the maximum number of uncrossed lines between two arrays, nums1 and nums2.
Dynamic programming is utilized to efficiently calculate the maximum number of uncrossed lines by considering subproblems and building up solutions from simpler cases.
The dp array is filled in a bottom-up manner, and at each step, the choice is made between extending the line from the previous elements or starting a new line.
The final result is stored in the last cell of the dp array, representing the maximum number of uncrossed lines between nums1 and nums2.
"""
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        # Initialize two arrays for dynamic programming
        dp = [0] * (n2 + 1)
        dpPrev = [0] * (n2 + 1)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                # If the current elements from both arrays are equal
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    # If not equal, choose the maximum value from the adjacent cells
                    dp[j] = max(dp[j - 1], dpPrev[j])

            # Update the previous dp array with the current one
            dpPrev = dp[:]

        # The result is stored in the last cell of the dp array
        return dp[n2]
