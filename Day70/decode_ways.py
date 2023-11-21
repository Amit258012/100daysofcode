# https://leetcode.com/problems/decode-ways/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The numDecodings function uses dynamic programming to count the number of ways to decode a given string.
It iterates through the string in reverse order, considering each digit and the possibility of combining it with the next digit.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # Initialize a dynamic programming dictionary to store the number of decodings for each position.
        dp = {len(s): 1}

        # Iterate through the string in reverse order.
        for i in range(len(s) - 1, -1, -1):
            # If the current digit is '0', there are no valid decodings.
            if s[i] == "0":
                dp[i] = 0
            else:
                # Initialize the number of decodings for the current position with the value at the next position.
                dp[i] = dp[i + 1]

            # Check if combining the current and next digits forms a valid decoding.
            if i + 1 < len(s) and (
                s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                dp[i] += dp[i + 2]

        # Return the number of decodings for the first position.
        return dp[0]
