"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.
"""

"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        # Handle edge cases for arrays of size 1 and 2.
        if n == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[n - 1] != nums[n - 2]:
            return nums[n - 1]

        # Initialize left and right pointers.
        l = 1
        h = n - 2

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                # If the element is not equal to its adjacent elements, it's the single non-duplicate.
                return nums[mid]

            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (
                mid % 2 == 1 and nums[mid] == nums[mid - 1]
            ):
                # Check if the non-duplicate element is on the right or left side and update pointers accordingly.
                l = mid + 1
            else:
                h = mid - 1
