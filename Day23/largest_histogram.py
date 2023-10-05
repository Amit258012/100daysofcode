# https://leetcode.com/problems/largest-rectangle-in-histogram

"""
Time complexity:- O(n)
Space Complexity:- O(n)
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []  # Stack to keep track of indices and heights
        n = len(heights)

        for i, h in enumerate(heights):
            start = i
            while stack and heights[i] < stack[-1][1]:
                idx, height = stack.pop()
                # Calculate the area using the popped height and the width (i - idx)
                maxArea = max(maxArea, height * (i - idx))
                start = idx  # Update the start index for the next iteration
            stack.append((start, h))  # Push the current index and height onto the stack

        # Calculate the remaining areas for elements left in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (n - i))

        return maxArea
