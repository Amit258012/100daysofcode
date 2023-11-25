# https://leetcode.com/problems/longest-common-subsequence/
"""
Time complexity:- O(N*M)
Space Complexity:- O(N*M) 
"""

"""
Intuition:

The problem involves finding the length of the longest common subsequence (LCS) between two strings.
Dynamic programming is used to efficiently calculate the LCS length by considering subproblems and building up solutions from simpler cases.
The dp array is filled in a bottom-up manner, starting from the end of both strings and iteratively calculating the LCS length by comparing characters.
The final result is the top-left cell of the dp array, representing the length of the LCS.
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initialize a 2D array for dynamic programming
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        # Fill in the dp array from bottom-right to top-left
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                # If the current characters match, increment the LCS length
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # If the characters are different, take the maximum of LCS lengths from the right and below
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # The result is the top-left cell of the dp array
        return dp[0][0]
