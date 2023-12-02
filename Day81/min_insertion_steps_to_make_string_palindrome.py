# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/
"""
Time complexity:- O(N^2)
Space Complexity:- O(N)
"""

"""
Intuition:

The code addresses the problem of finding the minimum number of insertions needed to make a string a palindrome.
Dynamic programming is utilized to efficiently compute the minimum insertions for each substring.
The 'dp' array is filled in a bottom-up manner, and at each step, the minimum insertions are updated based on the characters at positions i and j.
The final result is the minimum insertions needed for the entire string, stored in the last element of the 'dp' array.
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        # Get the length of the input string
        n = len(s)

        # Initialize an array 'dp' to store the minimum insertions for each substring
        dp = [0] * n

        # Iterate through the string in reverse order
        for i in range(n - 2, -1, -1):
            # Initialize a variable 'prev' to store the value of dp[j] before the update
            prev = 0

            # Iterate through the substring starting from i+1
            for j in range(i + 1, n):
                # Store the current value of dp[j] in a temporary variable 'temp'
                temp = dp[j]

                # Update dp[j] based on whether the characters at positions i and j are equal
                if s[i] == s[j]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1

                # Update 'prev' with the temporary variable 'temp'
                prev = temp

        # The result is the minimum insertions needed for the entire string
        return dp[n - 1]
