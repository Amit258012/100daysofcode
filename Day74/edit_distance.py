# https://leetcode.com/problems/edit-distance/
"""
Time complexity:- O(N*M)
Space Complexity:- O(N*M) 
"""

"""
Intuition:

The problem is a classic example of the edit distance problem, where the goal is to transform one string into another using a minimum number of operations (insertion, deletion, or substitution).
Dynamic programming is employed to find the minimum edit distance by considering subproblems and building up solutions from simpler cases.
The dp array is filled in a bottom-up manner, starting from the base cases and iteratively calculating the minimum number of operations required to transform substrings of the words.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Initialize a 2D array for dynamic programming
        dp = [[float("inf")] * (len(word2) + 1) for i in range(len(word1) + 1)]

        # Base cases: Initialize the last row and column of the dp array
        for j in range(len(word2) + 1):
            dp[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            dp[i][len(word2)] = len(word1) - i

        # Fill in the dp array from bottom-right to top-left
        for i in range(len(word1) - 1, -1, -1):
            for j in range(len(word2) - 1, -1, -1):
                # If the current characters match, no additional operation is needed
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    # If the characters are different, find the minimum of three operations
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j + 1], dp[i + 1][j + 1])

        # The result is the top-left cell of the dp array
        return dp[0][0]
