# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code checks if it's possible to partition the input array into three non-empty subarrays, satisfying specific conditions.
The 'dp' array is used to keep track of the possibility of forming subarrays with 2 equal elements, 3 equal elements, and 3 consecutive increasing elements.
The window is moved forward by updating the 'dp' array for each element in the input array.
The final result is whether it's possible to partition the array into valid subarrays, and it's determined by the value at dp[2].
"""

from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        # If the array has only one element, then not possible to partition into valid subarrays
        if n == 1:
            return False

        # Initialization for the first three values
        dp = [True, False, nums[0] == nums[1] if n > 1 else False]

        for i in range(2, n):
            current_dp = False

            # Check for 2 equal elements
            if nums[i] == nums[i - 1] and dp[1]:
                current_dp = True

            # Check for 3 equal elements
            elif nums[i] == nums[i - 1] == nums[i - 2] and dp[0]:
                current_dp = True

            # Check for 3 consecutive increasing elements
            elif (
                nums[i] - nums[i - 1] == 1 and nums[i - 1] - nums[i - 2] == 1 and dp[0]
            ):
                current_dp = True

            # Move the window forward
            dp[0], dp[1], dp[2] = dp[1], dp[2], current_dp

        return dp[2]
