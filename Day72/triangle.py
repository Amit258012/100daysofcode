# https://leetcode.com/problems/triangle/
"""
Time complexity:- O(N^2)
Space Complexity:- O(N) 
"""

"""
Intuition:


The function "minimumTotal" efficiently calculates the minimum path sum in a triangular structure of numbers. It starts from the bottom row and iterates upward, updating each element with the sum of its value and the minimum of the adjacent elements in the row below. This dynamic programming approach ensures that each element reflects the optimal path sum at each step. The final result, stored in the first element of the array, represents the minimum path sum from the bottom to the top of the triangle.
"""


from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start with the bottom row of the triangle.
        dp = triangle[-1]

        # Traverse the triangle from second-to-last row to the top.
        for row in range(len(triangle) - 2, -1, -1):
            # For each element in the current row, update it with the minimum sum from the next row.
            for col in range(0, row + 1):
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])

        # The first element of dp now contains the minimum path sum.
        return dp[0]
