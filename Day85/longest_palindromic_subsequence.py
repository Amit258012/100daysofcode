# https://leetcode.com/problems/longest-palindromic-subsequence/
"""
Time complexity:- O(n*m)
Space Complexity:- O(m)
"""

"""
Intuition:

The algorithm uses dynamic programming to find the length of the longest common subsequence (LCS) between the given string 's' and its reverse 't'.
The lcs function calculates the length of the LCS using a 2D dynamic programming approach.
The longestPalindromeSubseq function reverses the input string and then calculates the length of the LCS between the original and reversed strings.
The result is the length of the longest palindromic subsequence in the input string 's'.
"""


class Solution:
    def lcs(self, s1, s2):
        n = len(s1)
        m = len(s2)

        # Initialize two lists, prev and cur, for dynamic programming
        prev = [0] * (m + 1)
        cur = [0] * (m + 1)

        # Base Case is covered as we have initialized the prev and cur to 0.
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                if s1[ind1 - 1] == s2[ind2 - 1]:
                    cur[ind2] = 1 + prev[ind2 - 1]
                else:
                    cur[ind2] = max(prev[ind2], cur[ind2 - 1])
            prev = cur[:]  # Update prev to be a copy of cur for the next iteration

        # The final value in prev will be the length of the LCS
        return prev[m]

    def longestPalindromeSubseq(self, s: str) -> int:
        # Reverse the input string
        t = s[::-1]

        # Find the length of the longest common subsequence between s and its reverse
        return self.lcs(s, t)
