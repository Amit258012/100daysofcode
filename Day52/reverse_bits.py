# https://leetcode.com/problems/reverse-bits/

"""
Time complexity:- O(1)
Space Complexity:- O(1) 
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0  # Initialize a variable to store the reversed integer.

        # Iterate through the 32 bits in the integer.
        for i in range(32):
            # Extract the 'i'-th bit of 'n' by shifting and masking.
            bit = (n >> i) & 1
            # Place the extracted bit in the reversed integer, reversing its position.
            res = res | (bit << (31 - i))

        return res  # Return the reversed 32-bit integer.
