# https://leetcode.com/problems/sudoku-solver/
"""
Time complexity:- O(9^(n^2))
Space Complexity:- O(1) 
"""

"""
Intuition:

The solveSudoku method uses a backtracking approach to solve the Sudoku puzzle in-place.
The isValid function checks if a digit can be placed at a given position without violating the Sudoku rules.
The solve function recursively tries to fill in the Sudoku grid by considering each empty cell and trying digits from 1 to 9.
If a placement leads to a valid solution, the process continues; otherwise, it backtracks to the previous state and tries a different digit.
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
