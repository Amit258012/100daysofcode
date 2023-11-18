# https://leetcode.com/problems/frequency-of-the-most-frequent-element/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The algorithm aims to find the maximum frequency of any element in the array, given the ability to modify at most k elements.
The sliding window approach efficiently computes the sum of elements in the current window while ensuring the condition is met.
"""


from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array for efficient sliding window computation
        nums.sort()
        # Initialize pointers for the sliding window (left and right)
        left = 0
        # Initialize the result variable to store the maximum frequency
        res = 0
        # Initialize the sum of the current window
        cur = 0

        # Iterate over the array using the right pointer
        for right in range(len(nums)):
            # Get the target element in the current window
            target = nums[right]
            # Add the target element to the current sum
            cur += target

            # Check if the current window violates the condition (sum of differences > k)
            while (right - left + 1) * target - cur > k:
                # Remove the leftmost element from the window
                cur -= nums[left]
                left += 1

            # Update the result with the maximum frequency encountered so far
            res = max(res, right - left + 1)

        # The final result represents the maximum frequency achievable with at most k modifications
        return res
