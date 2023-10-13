# https://leetcode.com/problems/powx-n/
"""
Time complexity:- O(log n)
Space Complexity:- O(1)
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1.0
        nn = n

        # Handle negative exponent
        if nn < 0:
            nn = -1 * nn

        while nn:
            if nn % 2:  # If nn is odd
                ans = ans * x
                nn -= 1
            else:
                x = x * x
                nn = nn // 2  # Divide nn by 2

        if n < 0:
            return 1.0 / ans  # Invert the result for negative exponent
        return ans
