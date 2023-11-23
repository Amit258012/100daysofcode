# https://leetcode.com/problems/partition-equal-subset-sum/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The canPartition function checks if it's possible to partition the array into two subsets with equal sums.
It uses a dynamic programming approach, iteratively updating a set of possible subset sums.
"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Check if the sum of the array is odd, then partition is not possible.
        if sum(nums) % 2:
            return False

        # Initialize a set to store possible sums of subsets.
        dp = set()
        dp.add(0)

        # Calculate the target sum for each partition.
        target = sum(nums) // 2

        # Iterate through the array in reverse.
        for i in range(len(nums) - 1, -1, -1):
            # Initialize a new set for the next iteration.
            nextDP = set()

            # Iterate through the current set of possible sums.
            for t in dp:
                # If the current sum plus the current element equals the target,
                # it means partition is possible, and we return True.
                if (t + nums[i]) == target:
                    return True
                # Add the current sum plus the current element and the current sum to the new set.
                nextDP.add(t + nums[i])
                nextDP.add(t)

            # Update the set for the next iteration.
            dp = nextDP

        # If no partition is found, return False.
        return False
