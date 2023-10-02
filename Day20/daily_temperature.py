# https://leetcode.com/problems/daily-temperatures/

"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
"""
"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n  # Initialize a list to store the result (waiting periods)
        stack = []  # Initialize a stack to keep track of temperatures and their indices

        for i, t in enumerate(temp):
            # While the stack is not empty and the current temperature is greater than the temperature on top of the stack
            while stack and t > stack[-1][0]:
                # Get the temperature and index from the stack
                stack_temp, stack_idx = stack.pop()

                # Calculate the waiting period and store it in the result
                res[stack_idx] = i - stack_idx

            # Push the current temperature and its index onto the stack
            stack.append([t, i])

        return res
