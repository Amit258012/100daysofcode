# https://leetcode.com/problems/maximal-square/
"""
Time complexity:- O(M*N)
Space Complexity:- O(M*N)
"""

"""
Intuition:

The code uses dynamic programming with memoization to find the size of the largest square of 1s in the given matrix.
The helper function is a recursive function that calculates the maximum square size for each cell in the matrix.
The result is the area of the largest square found.
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {}  # Map each (r, c) -> maxLength of square

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0

            if (r, c) not in cache:
                # Recursively calculate the maximum square size considering three possible directions
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diag = helper(r + 1, c + 1)

                # Calculate the maximum square size for the current cell
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)
            return cache[(r, c)]

        # Start the recursive function from the top-left corner
        helper(0, 0)

        # Return the area of the largest square found
        return max(cache.values()) ** 2
