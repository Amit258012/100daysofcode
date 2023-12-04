# https://leetcode.com/problems/minimum-path-sum/
"""
Time complexity:- O(M*N)
Space Complexity:- O(N)
"""

"""
Intuition:

The code aims to find the minimum path sum from the top-left corner to the bottom-right corner of the grid.
It iterates through the grid in reverse order, updating the minimum path sums for each cell by considering the right and bottom neighbors.
The final result is stored in the first element of the prev list, representing the minimum path sum.
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        m, n = len(grid), len(grid[0])

        # Initialize a list to store the minimum path sum for each column in the last row
        prev = [float("inf")] * n
        prev[-1] = 0  # Set the last element to 0 as the starting point

        # Iterate through the grid from bottom to top and from right to left
        for row in range(m - 1, -1, -1):
            # Initialize a temporary list to store the minimum path sum for each column in the current row
            dp = [float("inf")] * n

            # Iterate through each column in the current row
            for col in range(n - 1, -1, -1):
                # Check if the current column is not the last one
                if col < n - 1:
                    # Update the minimum path sum for the current column by considering the right neighbor
                    dp[col] = min(dp[col], dp[col + 1])

                # Update the minimum path sum for the current column by considering the bottom neighbor
                dp[col] = min(dp[col], prev[col]) + grid[row][col]

            # Update the 'prev' list with the minimum path sum for each column in the current row
            prev = dp

        # The first element in the 'prev' list now contains the minimum path sum
        return prev[0]
