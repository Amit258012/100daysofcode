# https://leetcode.com/problems/surrounded-regions/
"""
Time complexity:- O(rows*cols) 
Space Complexity:- O(1)
"""

"""
Intuition:

The algorithm uses Depth-First Search (DFS) to mark 'O' regions connected to the borders as 'S'. After marking, the board is updated to replace 'S' with 'O' and other characters with 'X'.

Observation:

The dfs function recursively explores 'O' regions and marks them as 'S'.
The save list stores starting coordinates for DFS traversal, including the borders and inner coordinates.
The final board is updated by replacing 'S' with 'O' and other characters with 'X'.
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Check if the board is empty
        if not any(board):
            return

        # Get the number of rows and columns in the board
        m, n = len(board), len(board[0])

        # Helper function to perform DFS and mark 'O' regions as 'S'
        def dfs(i, j):
            # Check if the current coordinates are within bounds and contain 'O'
            if 0 <= i < m and 0 <= j < n and board[i][j] == "O":
                # Mark the current 'O' as 'S'
                board[i][j] = "S"
                # Explore adjacent coordinates using DFS
                dfs(i, j - 1)
                dfs(i, j + 1)
                dfs(i - 1, j)
                dfs(i + 1, j)

        # Starting DFS from the borders and marking 'O' regions as 'S'
        save = (
            [(0, k) for k in range(m + n)]
            + [(m - 1, k) for k in range(m + n)]
            + [(k, 0) for k in range(1, m - 1)]
            + [(k, n - 1) for k in range(1, m - 1)]
        )
        while save:
            i, j = save.pop()
            dfs(i, j)

        # Update the board by replacing 'S' with 'O' and other characters with 'X'
        board[:] = [["XO"[c == "S"] for c in row] for row in board]
