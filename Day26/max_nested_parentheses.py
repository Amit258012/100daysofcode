# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0  # Initialize a variable to store the maximum depth.
        openCount = 0  # Initialize a variable to keep track of open parentheses.

        # Iterate through each character in the string 's'.
        for ch in s:
            if ch == "(":
                openCount += 1  # Increment the openCount for an open parenthesis.
            elif ch == ")":
                openCount -= 1  # Decrement the openCount for a close parenthesis.

            # Update the maximum depth by taking the maximum of the current depth and res.
            res = max(res, openCount)

        return res  # Return the maximum depth found in the string.
