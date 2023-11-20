# https://leetcode.com/problems/house-robber/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The problem follows the dynamic programming approach.
At each step, the algorithm calculates the maximum value considering the two possibilities: robbing the current house or skipping it.
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # Iterate through the array, maintaining the maximum value considering skipping or robbing each house.
        for n in nums:
            # Calculate the maximum by either robbing the current house or skipping it.
            temp = max(n + rob1, rob2)
            rob1 = rob2  # Update rob1 to the previous rob2.
            rob2 = temp  # Update rob2 to the new maximum value.
        return rob2
