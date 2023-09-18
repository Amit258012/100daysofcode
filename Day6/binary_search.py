"""
Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
"""

"""
Time Complexity:- O(nlogn)
Space Complexity:- o(1)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0  # Initialize the left pointer.
        right = n - 1  # Initialize the right pointer.

        while left <= right:
            mid = (left + right) // 2  # Calculate the middle index.

            if nums[mid] == target:
                # If the middle element is equal to the target, return its index.
                return mid

            elif target > nums[mid]:
                # If the target is greater than the middle element, search in the right half.
                left = mid + 1

            else:
                # If the target is smaller than the middle element, search in the left half.
                right = mid - 1

        return -1  # Return -1 if the target element is not found in the list.
