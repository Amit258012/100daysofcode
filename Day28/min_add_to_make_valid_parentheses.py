# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = bal = 0

        # Iterate through each character in the input string.
        for ch in s:
            if ch == "(":
                bal += 1
            else:
                bal -= 1

            # If the balance becomes -1 (closing parenthesis without a corresponding open parenthesis),
            # it means we need to add an open parenthesis to balance it.
            if bal == -1:
                ans += 1
                bal += 1

        # The answer is the sum of unmatched open and close parentheses (balance).
        return ans + bal
