# https://leetcode.com/problems/sum-of-two-integers/

"""
Time complexity:- O(1)
Space Complexity:- O(1) 
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # Initialize a mask to 32 bits (0xffffffff in hexadecimal).

        while (b & mask) > 0:
            # Calculate the carry bit using bitwise AND and left shift.
            carry = (a & b) << 1
            a = a ^ b  # Calculate the sum of 'a' and 'b' using bitwise XOR.
            b = carry  # Update 'b' with the carry bit.

        return (a & mask) if b > 0 else a  # Return the result, considering overflow.
