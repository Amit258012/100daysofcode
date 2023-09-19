"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
"""

"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Get the length of the input list 'nums'.
        n = len(nums)

        # Initialize the left and right pointers for binary search.
        left = 0
        right = n - 1

        while left <= right:
            # Calculate the middle index.
            mid = (left + right) // 2

            if nums[mid] == target:
                # If the middle element is equal to the target, return True.
                return True

            # Handle the case where nums[left], nums[mid], and nums[right] are equal.
            if nums[mid] == nums[left] and nums[mid] == nums[right]:
                left += 1
                right -= 1
                continue

            # Check if the left half is sorted.
            if nums[left] <= nums[mid]:
                if nums[left] <= target and target <= nums[mid]:
                    # If the target is in the left half, update the right pointer.
                    right = mid - 1
                else:
                    # If the target is in the right half, update the left pointer.
                    left = mid + 1
            else:
                # The right half is sorted.
                if nums[mid] <= target and target <= nums[right]:
                    # If the target is in the right half, update the left pointer.
                    left = mid + 1
                else:
                    # If the target is in the left half, update the right pointer.
                    right = mid - 1

        # If the target is not found, return False.
        return False
