# https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/
"""
Time complexity:- O(N logN)
Space Complexity:- O(1) 
"""

"""
Intuition:

The goal is to find the number of operations needed to make all elements in the array equal.
Sorting the array helps identify distinct values and their frequencies.
The algorithm counts the number of increments needed to reach the next distinct element and accumulates the total operations.
"""

from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # Sort the array in ascending order.
        nums.sort()

        ans = 0  # Initialize the result.
        up = 0  # Counter for the number of increments.

        # Iterate through the array starting from the second element.
        for i in range(1, len(nums)):
            # If the current element is different from the previous one,
            # increment the 'up' counter.
            if nums[i] != nums[i - 1]:
                up += 1
            # Add the current 'up' value to the result.
            ans += up

        return ans
