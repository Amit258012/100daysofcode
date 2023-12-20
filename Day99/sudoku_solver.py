# https://leetcode.com/problems/sudoku-solver/
"""
Time complexity:- O(9^(n^2))
Space Complexity:- O(1) 
"""

"""
Intuition:

The findMaxForm method uses dynamic programming to solve the 0/1 knapsack problem.
The DP array dp[i][j] represents the maximum number of strings that can be formed with i '0's and j '1's.
The counter list stores the count of '0's and '1's for each string in the input list strs.
The nested loops iterate through each string and update the DP array based on the counts of '0's and '1's, maximizing the count.
The result is obtained from the bottom-right cell of the DP array.
"""


from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = 9

        def isValid(row, col, ch):
            row, col = int(row), int(col)

            # Check if the current digit 'ch' is valid in the row, column, and 3x3 grid
            for i in range(9):
                if board[i][col] == ch:
                    return False
                if board[row][i] == ch:
                    return False
                if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == ch:
                    return False

            return True

        def solve(row, col):
            if row == n:
                return True
            if col == n:
                return solve(row + 1, 0)

            if board[row][col] == ".":
                # Try placing digits 1 to 9 and check if the placement is valid
                for i in range(1, 10):
                    if isValid(row, col, str(i)):
                        board[row][col] = str(i)

                        # Recursively try to solve the remaining board
                        if solve(row, col + 1):
                            return True
                        else:
                            # Backtrack if the current placement leads to an invalid solution
                            board[row][col] = "."
                return False
            else:
                # If the current cell already has a digit, move to the next cell
                return solve(row, col + 1)

        # Start solving the Sudoku puzzle from the top-left corner
        solve(0, 0)
