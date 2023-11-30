# https://leetcode.com/problems/unique-paths/
"""
Time complexity:- O(M*N) M = rows and N = col
Space Complexity:- O(N)
"""

"""
Intuition:

The code addresses the problem of finding the number of unique paths from the top-left corner to the bottom-right corner in a grid.
Dynamic programming is utilized to efficiently calculate the number of paths by considering the paths from the above cell and the left cell.
The 'prev' array is used to store intermediate results for the previous row, and the 'temp' array is used to store the current row results.
The final result is the number of unique paths stored in the last element of the 'prev' array
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a previous row to store intermediate results.
        prev = [0] * n

        # Loop through each row of the grid.
        for i in range(m):
            # Initialize a temporary row to store current row results.
            temp = [0] * n

            # Loop through each column of the grid.
            for j in range(n):
                # Base case: If we are at the top-left corner, there is one way to reach it.
                if i == 0 and j == 0:
                    temp[j] = 1
                    continue

                # Initialize variables to store the number of ways from above and from the left.
                up = 0
                left = 0

                # Check if moving up is a valid option (not out of bounds).
                if i > 0:
                    up = prev[j]

                # Check if moving left is a valid option (not out of bounds).
                if j > 0:
                    left = temp[j - 1]

                # Calculate and store the number of ways to reach the current cell.
                temp[j] = up + left

            # Update the previous row with the current row results.
            prev = temp

        # The last element in the previous row (prev) now contains the total number of ways to reach the destination.
        return prev[n - 1]
