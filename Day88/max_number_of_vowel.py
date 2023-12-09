# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The algorithm uses a sliding window approach to efficiently count vowels in each window of size 'k'.
It maintains a count of vowels in the current window and updates the count when moving the window.
The maximum count of vowels is tracked, and the result is updated accordingly.
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelsCount = 0  # Variable to store the count of vowels in the current window
        res = 0  # Variable to store the maximum count of vowels
        n = len(s)  # Length of the input string

        for r in range(n):
            if r >= k:
                # If the window size exceeds 'k', remove the leftmost character from the window
                if s[r - k] in "aeiou":
                    vowelsCount -= 1

            # Add the current character to the window
            if s[r] in "aeiou":
                vowelsCount += 1

            # Update the maximum count of vowels
            res = max(res, vowelsCount)

        return res
