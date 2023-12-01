# https://leetcode.com/problems/unique-paths-ii/
"""
Time complexity:- O(M*N) M = rows and N = col
Space Complexity:- O(N)
"""

"""
Intuition:

The code addresses the problem of finding the number of unique paths from the top-left to the bottom-right cell in a grid with obstacles.
Dynamic programming is utilized to efficiently calculate the number of unique paths by considering the paths from the left cell and the above cell.
The 'previous' and 'current' arrays are used to store the number of unique paths for each cell in the current and previous rows, respectively.
The final result is the number of unique paths for the bottom-right cell, which is stored in the last element of the 'previous' array.
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Check if the grid is empty or the top-left cell is an obstacle
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0

        # Get the dimensions of the grid
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Initialize two arrays to store the number of unique paths for each cell in the current and previous rows
        previous = [0] * n
        current = [0] * n
        previous[0] = 1  # There is one way to reach the top-left cell

        # Iterate through each row
        for i in range(m):
            # Calculate the number of unique paths for the first cell in the current row
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]

            # Iterate through each column starting from the second cell
            for j in range(1, n):
                # Calculate the number of unique paths for the current cell based on the obstacles
                current[j] = (
                    0 if obstacleGrid[i][j] == 1 else current[j - 1] + previous[j]
                )

            # Update the 'previous' array with the values of the 'current' array for the next iteration
            previous[:] = current

        # The result is the number of unique paths for the bottom-right cell
        return previous[n - 1]
