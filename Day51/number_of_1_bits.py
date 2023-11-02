# https://leetcode.com/problems/number-of-1-bits/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0  # Initialize a count to keep track of the number of '1' bits.

        # Continue the loop until 'n' becomes zero.
        while n:
            n = n & (n - 1)  # Clear the least significant '1' bit using bitwise AND.
            count += 1  # Increment the count for each cleared '1' bit.

        return count  # Return the total count of '1' bits in the binary representation of 'n'.
