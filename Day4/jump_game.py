"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # The goal is to reach the end of the list.

        # Iterate through the list in reverse order.
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                # If it's possible to jump from the current position to or beyond the goal,
                # update the goal to the current position.
                goal = i

        # If the goal reaches the beginning of the list, it means it's possible to reach the end.
        return goal == 0
