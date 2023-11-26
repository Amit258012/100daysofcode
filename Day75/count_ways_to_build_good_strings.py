# https://leetcode.com/problems/count-ways-to-build-good-strings/
"""
Time complexity:- O(high)
Space Complexity:- O(high) 
"""

"""
Intuition:

The code aims to count the number of good strings of lengths within the range [low, high].
Dynamic programming is used to efficiently calculate the number of good strings for each length up to high.
The dp array is iteratively filled, considering the possibilities of appending zero 0s or one 1s to form good strings.
The final result is obtained by summing up the counts for lengths within the specified range and taking the result modulo 10^9 + 7.
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        # Use dp[i] to record the number of good strings of length i.
        dp = [1] + [0] * (high)
        mod = 10**9 + 7

        # Iterate over each length `end`.
        for end in range(1, high + 1):
            # Check if the current string can be made by appending zero `0`s or one `1`s.
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod

        # Add up the number of strings with each valid length [low ~ high].
        return sum(dp[low : high + 1]) % mod
