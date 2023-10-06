# https://leetcode.com/problems/next-greater-element-ii

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []  # Initialize an empty stack to keep track of indices
        n = len(nums)  # Get the length of the input list
        res = [-1] * n  # Initialize the result list with -1 for all elements

        for i, num in enumerate(nums):  # Iterate through the list
            while stack and nums[stack[-1]] < num:
                # While the stack is not empty and the current element is greater
                # than the element at the index stored at the top of the stack,
                # update the result for that index and pop the index from the stack.
                res[stack.pop()] = num
            stack.append(i)  # Push the current index onto the stack

        # Iterate through the list again to handle the circular property (second pass)
        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num

        return res  # Return the list containing the next greater elements
