# https://leetcode.com/problems/maximum-product-subarray/
"""
Time complexity:- O(N*M) 
Space Complexity:- O(N) 
"""

"""
Intuition:

The wordBreak function uses dynamic programming to determine if the given string can be segmented into words from the dictionary.
It iterates through the string, checking if substrings can be segmented based on the words in the dictionary.
"""


from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize an array to store whether a substring from index i to the end can be segmented.
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # An empty substring is always segmentable.

        # Iterate through the string in reverse.
        for i in range(len(s) - 1, -1, -1):
            # Check if any word in the dictionary matches the current substring.
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Update dp[i] based on dp[i + len(w)].
                if dp[i]:
                    break  # If dp[i] is True, no need to check other words.

        # Return whether the entire string can be segmented.
        return dp[0]
