# https://leetcode.com/problems/single-number/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""


class Solution:
    def singleNumber(self, nums):
        res = 0  # Initialize a variable to store the result.

        # Iterate through the elements in the 'nums' list.
        for n in nums:
            res ^= n  # Perform a bitwise XOR operation with the current element 'n' and update the result 'res'.

        return res  # Return the final result, which is the XOR of all elements in the 'nums' list.
