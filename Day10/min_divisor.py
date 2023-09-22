"""
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.
"""

"""
Time Complexity:- O(nlog(max))
Space Complexity:- o(1)
"""


import math
from typing import List


class Solution:
    def sum_of_div(self, nums, divisor):
        total = 0
        for num in nums:
            total += math.ceil(num / divisor)
        return total

    def smallest_divisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        h = max(nums)
        n = len(nums)

        while l <= h:
            mid = (l + h) // 2

            if self.sum_of_div(nums, mid) <= threshold:
                h = mid - 1
            else:
                l = mid + 1

        return l
