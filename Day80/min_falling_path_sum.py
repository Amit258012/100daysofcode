# https://leetcode.com/problems/minimum-falling-path-sum/
"""
Time complexity:- O(M*N) M = rows and N = col
Space Complexity:- O(M*N)
"""

"""
Intuition:

The code addresses the problem of finding the minimum falling path sum in a 2D array.
Dynamic programming is utilized to efficiently calculate the minimum falling path sum for each cell by considering the adjacent cells in the previous row.
The 'dp' array is filled in a bottom-up manner, and at each step, the minimum falling path sum for the current cell is updated based on the values of adjacent cells in the previous row.
The final result is the minimum falling path sum from the last row, which is obtained by finding the minimum value in the last row of the 'dp' array.
"""
from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        # Get the dimensions of the array
        m, n = len(arr), len(arr[0])

        # Check if the array is empty
        if m == 0 or n == 0:
            return 0

        # Initialize a 2D array 'dp' to store the minimum falling path sum for each cell
        dp = [[None] * n for r in range(m)]

        # Iterate through each row and column
        for i in range(m):
            for j in range(n):
                # Base case: When it's the first row, the falling path sum is the same as the array value
                if i == 0:
                    dp[i][j] = arr[i][j]
                # When there is only one column
                elif j == 0 and j == n - 1:
                    dp[i][j] = arr[i][j] + dp[i - 1][j]
                # When it is the first column, (column-1) will be out of bounds
                elif j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + arr[i][j]
                # When it is the last column, (column+1) will be out of bounds
                elif j == n - 1:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + arr[i][j]
                # Choose the minimum from the three adjacent cells
                else:
                    dp[i][j] = (
                        min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])
                        + arr[i][j]
                    )

        # Return the minimum falling path sum from the last row
        return min(dp[-1])
