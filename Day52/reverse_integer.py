# https://leetcode.com/problems/reverse-integer/

"""
Time complexity:- O(logN)
Space Complexity:- O(1) 
"""


import math


class Solution:
    def reverse(self, x: int) -> int:
        # Define the minimum and maximum bounds for a 32-bit signed integer.
        MIN = -2147483648  # -2^31,
        MAX = 2147483647  # 2^31 - 1

        res = 0  # Initialize the result variable to store the reversed integer.

        # Perform the digit reversal and overflow checks in a loop.
        while x:
            digit = int(math.fmod(x, 10))  # Extract the last digit using modulo.
            x = int(x / 10)  # Remove the last digit by integer division.

            # Check for overflow conditions:
            if res > MAX // 10 or (res == MAX // 10 and digit > MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and digit < MIN % 10):
                return 0

            # Update the result by appending the extracted digit.
            res = (res * 10) + digit

        return res  # Return the reversed integer.
