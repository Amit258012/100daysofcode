# https://leetcode.com/problems/excel-sheet-column-number/
"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0  # Initialize the result.

        for i, ch in enumerate(columnTitle):
            # Calculate the value of the current character and add it to the result.
            # You're treating it as a base-26 number, where 'A' represents 1, 'B' represents 2, and so on.
            # 'A' has ASCII code 65, so subtracting 64 gets the desired value.
            ans = ans * 26 + (ord(ch) - 64)

        return ans  # Return the final result.
