"""
Given an integer array nums, find the subarray
with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

"""


class Solution:
    def maxSubArray(self, nums):
        # Initialize variables to keep track of the maximum sum and the current sum.
        max_sum = float("-inf")
        current_sum = 0

        # Iterate through the array to find the maximum subarray sum.
        for num in nums:
            # If the current subarray sum is negative, start a new subarray.
            # Otherwise, continue adding elements to the current subarray.
            current_sum = max(num, current_sum + num)

            # Update the maximum subarray sum if needed.
            max_sum = max(max_sum, current_sum)

        # Return the maximum subarray sum found.
        return max_sum
