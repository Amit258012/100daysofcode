# https://leetcode.com/problems/house-robber-ii/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The rob function considers three scenarios: robbing the first house, robbing the last house, or skipping the first and last houses and considering all the middle houses.
For each scenario, the helper function is used to calculate the maximum value by either robbing or skipping each house.
"""


from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Return the maximum of three cases:
        # 1. Rob the first house and consider the rest of the houses (exclude the last one).
        # 2. Rob the last house and consider the rest of the houses (exclude the first one).
        # 3. Skip the first and last houses and consider all the middle houses.
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        # Iterate through the array, maintaining the maximum value considering skipping or robbing each house.
        for n in nums:
            # Calculate the maximum by either robbing the current house or skipping it.
            newRob = max(rob1 + n, rob2)
            rob1 = rob2  # Update rob1 to the previous rob2.
            rob2 = newRob  # Update rob2 to the new maximum value.
        return rob2
