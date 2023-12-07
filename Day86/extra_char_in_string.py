# https://leetcode.com/problems/extra-characters-in-a-string/
"""
Time complexity:- O(N^2)
Space Complexity:- O(N)
"""

"""
Intuition:

The function aims to find the minimum number of extra characters needed to make the given string s from the provided dictionary.
It uses dynamic programming to iterate through the string and considers all possible substrings.
The dp array is used to store the minimum number of extra characters needed for each substring.
The function starts iterating from the end of the string, updating the dp array for each character and substring.
The final result is the minimum number of extra characters needed for the entire string.
"""


from typing import List


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        # Convert the dictionary to a set for efficient lookup
        dictionary_set = set(dictionary)
        # Initialize an array to store the minimum number of extra characters needed
        dp = [0] * (len(s) + 1)

        # Iterate over the characters in reverse order
        for start in range(n - 1, -1, -1):
            # Initialize the minimum number of extra characters for the current substring
            dp[start] = 1 + dp[start + 1]
            # Check all possible substrings starting from the current character
            for end in range(start, n):
                # Extract the current substring
                curr = s[start : end + 1]
                # Check if the current substring is in the dictionary
                if curr in dictionary_set:
                    # Update the minimum number of extra characters needed
                    dp[start] = min(dp[start], dp[end + 1])

        # The final result is the minimum number of extra characters needed for the entire string
        return dp[0]
