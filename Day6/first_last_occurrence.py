"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

"""


from typing import List


####*: Brute Force
class Solution:
    """
    Time Complexity:- O(n)
    Space Complexity:- O(1)
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Initialize variables to store the first and last occurrences of the target.
        first = -1
        last = -1
        n = len(nums)

        # Iterate through the list to find the first and last occurrences.
        for i in range(n):
            if nums[i] == target:
                # If it's the first occurrence, update the 'first' index.
                if first == -1:
                    first = i
                # Always update the 'last' index to keep track of the last occurrence.
                last = i

        # Return the first and last occurrences as a list.
        return [first, last]


####*: Optimal
class Solution:
    """
    Time Complexity:- O(logn)
    Space Complexity:- O(1)
    """

    def firstPos(self, nums: List[int], target: int) -> int:
        # Helper function to find the first occurrence of the target.
        n = len(nums)
        low = 0
        high = n - 1
        first = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                first = mid
                high = mid - 1  # Move left to search for the first occurrence.
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return first

    def lastPos(self, nums: List[int], target: int) -> int:
        # Helper function to find the last occurrence of the target.
        n = len(nums)
        low = 0
        high = n - 1
        last = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                last = mid
                low = mid + 1  # Move right to search for the last occurrence.
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return last

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Call the helper functions to find the first and last occurrences.
        first = self.firstPos(nums, target)

        # If the first occurrence is not found, return [-1, -1].
        if first == -1:
            return [-1, -1]

        last = self.lastPos(nums, target)

        return [first, last]
