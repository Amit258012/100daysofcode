# https://leetcode.com/problems/minimize-maximum-of-array/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code iterates through the array and calculates the prefix sum at each step.
It calculates the average value for the current prefix sum and rounds it up using math.ceil.
The answer is updated with the maximum of the current answer and the calculated average value.
"""


import math
from typing import List


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # Initialize answer and the prefix sum.
        answer = 0
        prefixSum = 0

        # Iterate over nums, update prefix sum and answer.
        for i in range(len(nums)):
            prefixSum += nums[i]
            # Calculate the average value and round up using math.ceil.
            avg = math.ceil(prefixSum / (i + 1))
            # Update the answer with the maximum of current answer and average value.
            answer = max(answer, avg)

        # Return the minimum possible value of the array.
        return answer
