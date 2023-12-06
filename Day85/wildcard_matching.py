# https://leetcode.com/problems/wildcard-matching/
"""
Time complexity:- O(n*m)
Space Complexity:- O(n*m)
"""

"""
Intuition:

The algorithm uses a dynamic programming approach to solve the wildcard matching problem.
The DP table is filled based on the matching conditions for characters and wildcard '*' in the given strings.
The result is determined by checking the bottom-right cell of the DP table.
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Initialize a 2D DP table with False values
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]

        # Empty pattern matches empty string
        dp[0][0] = True

        # Handle '*' in the pattern for the empty string
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        # Fill the DP table using bottom-up dynamic programming
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                # Check if the characters match or pattern has '?', '*' at the current positions
                dp[i][j] = (p[j - 1] in [s[i - 1], "?", "*"] and dp[i - 1][j - 1]) or (
                    p[j - 1] == "*" and (dp[i][j - 1] or dp[i - 1][j])
                )

        # The result is stored in the bottom-right cell of the DP table
        return dp[len(s)][len(p)]
