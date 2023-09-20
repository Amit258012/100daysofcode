"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
"""

"""
Time Complexity:- O(logn)
Space Complexity:- o(1)
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Get the length of the input list 'nums'.
        n = len(nums)

        # Initialize the left and right pointers and set 'ans' to positive infinity.
        left = 0
        right = n - 1
        ans = float("inf")

        while left <= right:
            # Calculate the middle index.
            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                # If the left half is sorted, update 'ans' with the minimum of 'ans' and nums[left].
                ans = min(ans, nums[left])
                left = mid + 1
            else:
                # The right half is sorted, so update 'ans' with the minimum of 'ans' and nums[mid].
                ans = min(ans, nums[mid])
                right = mid - 1

        # Return the minimum value found.
        return ans
