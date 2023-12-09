# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The algorithm uses a sliding window approach to find the maximum subarray sum equal to the total sum minus the target sum.
It maintains a window sum and adjusts the window size by moving the left pointer when the sum exceeds the target.
The maximum subarray length is tracked, and the minimum number of operations is calculated accordingly.
"""


from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_val = sum(nums)  # Calculate the total sum of the array

        max_length = -1  # Variable to store the maximum subarray length
        curr_sum = 0  # Variable to store the current subarray sum
        l = 0  # Left pointer for the sliding window

        for r in range(len(nums)):
            curr_sum += nums[r]

            # Shrink the window from the left if the current sum exceeds the target sum
            while l <= r and curr_sum > sum_val - x:
                curr_sum -= nums[l]
                l += 1

            # Check if the current subarray sum is equal to the target sum
            if curr_sum == sum_val - x:
                max_length = max(max_length, r - l + 1)

        # Calculate the minimum number of operations needed to achieve the target sum
        return -1 if max_length == -1 else len(nums) - max_length
