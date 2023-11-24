# https://leetcode.com/problems/delete-and-earn/
"""
Time complexity:- O(N)
Space Complexity:- O(UpperLimit) 
"""

"""
Intuition:

The store array is created to accumulate the sum of values at each index. This helps in avoiding adjacent elements when choosing which elements to delete and earn points.

The dp array is then used to store the maximum points at each index. The decision at each step is whether to include the current element in the sum or skip it, considering the constraint of not having adjacent elements.

The dynamic programming recurrence relation dp[i] = max(dp[i - 2] + store[i], dp[i - 1]) captures the essence of the problem. It considers the maximum points up to the current index, either by including the current element or by skipping it.

The final result is the maximum value in the dp array, representing the maximum points that can be earned by deleting and earning at each step.
"""

from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Find the upper limit of the array
        upperLimit = max(nums) + 1

        # Create an array to store the sum of values at each index
        store = [0] * upperLimit

        # Populate the store array with the sum of values at each index
        for num in nums:
            store[num] += num

        # Initialize an array for dynamic programming
        dp = [0] * upperLimit

        # Base case: set the value for index 1
        dp[1] = 1 * store[1]

        # Iterate through the rest of the array to fill the dp array
        for i in range(2, upperLimit):
            # Choose the maximum value between skipping the current index and
            # adding the current index value to the previous non-adjacent value
            dp[i] = max(dp[i - 2] + store[i], dp[i - 1])

        # The final result is the last value in the dp array
        return dp[-1]
