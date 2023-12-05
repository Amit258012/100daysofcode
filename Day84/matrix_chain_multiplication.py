# https://practice.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1
"""
Time complexity:- O(N^3)
Space Complexity:- O(N^2)
"""

"""
Intuition:

The dynamic programming approach is used to find the optimal way to parenthesize matrices to minimize the number of scalar multiplications.
The 'dp' array is filled diagonally, starting with matrices of size 2x2 and gradually moving to larger matrices.
The innermost loop iterates over possible split points ('k') within the current range, and the cost of multiplying matrices is calculated.
The goal is to find the optimal split point that minimizes the overall cost of multiplication.
The final result is stored in the top-right cell of the 'dp' matrix, representing the minimum cost of multiplying all matrices.
"""


class Solution:
    def matrixMultiplication(self, n, arr):
        # Initialize a 2D array 'dp' to store the minimum number of scalar multiplications
        dp = [[0] * n for i in range(n)]

        # Iterate over the diagonals of the matrix
        for l in range(2, n):
            # As we move ahead, both row (r) and column (c) are incremented by 1
            c = l
            for r in range(0, n - l):
                # Initialize the current cell with positive infinity
                dp[r][c] = float("inf")

                # Iterate over the possible split points 'k' within the current range (r, c)
                for k in range(r + 1, c):
                    # Calculate the cost of multiplying the matrices and update the minimum
                    dp[r][c] = min(
                        dp[r][c], dp[r][k] + dp[k][c] + arr[r] * arr[k] * arr[c]
                    )

                # Move to the next column
                c += 1

        # The result is stored in the top-right cell of the 'dp' matrix
        return dp[0][n - 1]
