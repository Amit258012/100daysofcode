"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

"""
Time Complexity:- O(n)
Space Complexity:- O(1)
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0  # Initialize a count for the number of jumps.
        left = right = 0  # Initialize pointers for the current range.

        while right < len(nums) - 1:
            farthest = 0  # Initialize a variable to track the farthest position that can be reached.

            # Iterate through the current range [left, right].
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])

            left = right + 1  # Move the left pointer to the next range.
            right = (
                farthest  # Update the right pointer to the farthest position reached.
            )
            count += 1  # Increment the jump count.

        return count
