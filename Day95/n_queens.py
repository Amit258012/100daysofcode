# https://leetcode.com/problems/n-queens/
"""
Time complexity:- O(N!)
Space Complexity:- O(N)
"""

"""
Intuition:

The code uses a backtracking approach to explore all possible configurations of placing queens on the chessboard.
Sets (col, posDiag, negDiag) are used to keep track of occupied columns and diagonals.
The backtrack function recursively tries to place queens in each row while checking for conflicts.
When a valid configuration is found, it is added to the result list.
Backtracking involves undoing the changes to explore other possibilities.
"""


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()  # Set to track occupied columns
        posDiag = set()  # Set to track occupied positive diagonals (r + c)
        negDiag = set()  # Set to track occupied negative diagonals (r - c)

        res = []  # List to store the final solutions
        board = [["."] * n for i in range(n)]  # Chessboard represented as a 2D array

        def backtrack(r):
            # If we have placed queens in all rows, add the current board configuration to the result
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                # Check if the current position is safe for placing a queen
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Mark the current position as occupied
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Recursively move to the next row
                backtrack(r + 1)

                # Backtrack: undo the changes made to explore other possibilities
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        # Start the backtracking process from the first row (row 0)
        backtrack(0)
        return res
