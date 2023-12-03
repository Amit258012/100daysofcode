# https://leetcode.com/problems/interleaving-string/
"""
Time complexity:- O(N * M)
Space Complexity:- O(N * M)
"""

"""
Intuition:

The code addresses the problem of determining whether a third string (s3) can be formed by interleaving characters from two given strings (s1 and s2) while preserving the order of characters.
Dynamic programming is used to efficiently check all possible interleavings and store intermediate results in the 'dp' array.
The final result is determined by checking whether the entire s3 can be formed by interleaving characters from s1 and s2.
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # Check if the lengths of s1, s2, and s3 satisfy the interleave condition
        if len(s1) + len(s2) != len(s3):
            return False

        # Initialize a 2D array 'dp' to store whether a given substring is an interleaving of s1 and s2
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)]

        # Set the base case where empty substrings of s1 and s2 are interleaved to an empty s3
        dp[len(s1)][len(s2)] = True

        # Iterate through the substrings of s1 and s2 in reverse order
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                # Check if the current characters match and the substring to the right or below is an interleaving
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        # The result is stored in the top-left corner of the 'dp' array
        return dp[0][0]
