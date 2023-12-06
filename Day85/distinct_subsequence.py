# https://leetcode.com/problems/distinct-subsequences/
"""
Time complexity:- O(n*m)
Space Complexity:- O(m)
"""

"""
Intuition:

The algorithm uses dynamic programming to count the number of distinct subsequences of string 't' in string 's'.
The 'prev' list is used to store the number of distinct subsequences for each length of the prefix of string 't'.
The algorithm iterates through both strings in reverse order and updates the 'prev' list based on the matching characters. The final result is stored in 'prev[m]'.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        prime = int(1e9 + 7)
        m = len(t)
        n = len(s)

        # Initialize a list to store the previous row of the DP table
        prev = [0 for i in range(m + 1)]

        # Initialize the first element of prev to 1, as there's always one way to match an empty s2
        prev[0] = 1

        # Loop through s1 and s2 in reverse direction
        for i in range(1, n + 1):
            for j in range(m, 0, -1):
                # If the current characters match, update prev[j] based on previous values
                if s[i - 1] == t[j - 1]:
                    prev[j] = (prev[j - 1] + prev[j]) % prime
                # If the characters don't match, keep prev[j] unchanged (omit this statement)
                else:
                    prev[j] = prev[j]

        # The final value in prev[m] is the count of distinct subsequences
        return prev[m]
