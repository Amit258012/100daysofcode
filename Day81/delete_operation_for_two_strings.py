# https://leetcode.com/problems/delete-operation-for-two-strings/
"""
Time complexity:- O(M*N)
Space Complexity:- O(M*N)
"""

"""
Intuition:

The code addresses the problem of finding the minimum distance between two words by calculating the length of their common subsequence.
Dynamic programming is utilized to efficiently compute the lengths of common subsequences for each prefix of the two words.
The result is then calculated based on the lengths of the two words and twice the length of their common subsequence.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Get the lengths of the two words
        m = len(word1)
        n = len(word2)

        # Initialize a 2D array 'a' to store the length of the common subsequence for each prefix
        a = [[0] * (n + 1) for _ in range(m + 1)]

        # Populate the array 'a' using dynamic programming
        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    a[i + 1][j + 1] = 1 + a[i][j]
                else:
                    a[i + 1][j + 1] = max(a[i][j + 1], a[i + 1][j])

        # The result is the sum of the lengths of the two words minus twice the length of their common subsequence
        return m + n - (2 * a[-1][-1])
