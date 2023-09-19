"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

"""
Time Complexity:- O(n)
Space Complexity:- o(1)
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            n = abs(n)
            if nums[n] < 0:
                return n
            nums[n] *= -1
