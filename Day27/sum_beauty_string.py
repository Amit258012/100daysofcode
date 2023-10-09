# https://leetcode.com/problems/sum-of-beauty-of-all-substrings/

"""
Time complexity:- O(n^2)
Space Complexity:- O(n)
"""


class Solution:
    def beautySum(self, s: str) -> int:
        res = 0  # Initialize the result variable.
        n = len(s)  # Get the length of the input string.

        for i in range(0, n - 2):
            d = {}  # Create an empty dictionary to store character counts.
            for j in range(i, n):
                # Count occurrences of characters in the substring.
                d[s[j]] = 1 + d.get(s[j], 0)

                # Calculate the difference between the most and least frequent characters.
                diff = max(d.values()) - min(d.values())

                res += diff  # Add the difference to the result.

        return res  # Return the final result.
