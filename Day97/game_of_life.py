# https://leetcode.com/problems/game-of-life/
"""
Time complexity:- O(M *N)
Space Complexity:- O(1)
"""

"""
Intuition:

The gameOfLife method follows the rules of Conway's Game of Life to update the given board.
It uses a temporary state (-1 and 2) to represent changes in the current state.
The directions list represents the eight possible directions to check neighbors.
The live neighbors are counted based on the rules, and the temporary states are assigned accordingly.
Finally, the board is updated based on the temporary values.
"""
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]

        for i in range(len(board)):
            for j in range(len(board[0])):
                live = 0  # live neighbors count

                # Check and count neighbors in all directions
                for x, y in directions:
                    if (
                        (0 <= i + x < len(board))
                        and (0 <= j + y < len(board[0]))
                        and abs(board[i + x][j + y]) == 1
                    ):
                        live += 1

                # Apply rules
                if board[i][j] == 1 and (live < 2 or live > 3):  # Rule 1 or Rule 3
                    board[i][j] = -1
                if board[i][j] == 0 and live == 3:  # Rule 4
                    board[i][j] = 2

        # Update board based on the temporary values
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1 if board[i][j] > 0 else 0
