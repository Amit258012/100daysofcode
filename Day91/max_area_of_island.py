# https://leetcode.com/problems/max-area-of-island/
"""
Time complexity:- O(rows*cols) 
Space Complexity:- O(rows*cols)
"""

"""
Intuition:

DFS is used to traverse the grid and explore each island by recursively visiting adjacent cells. The maxAreaOfIsland function iterates through each cell, initiates DFS for unvisited islands, and updates the maximum area.

Observation:

The DFS function recursively explores the island by checking adjacent cells.
The visit set is used to keep track of visited cells to avoid redundant exploration.
"""
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Get the number of rows and columns in the grid
        ROWS, COLS = len(grid), len(grid[0])
        # Set to store visited cells
        visit = set()

        # Depth-First Search (DFS) function to explore the island
        def dfs(r, c):
            # Base cases: out of bounds or water cell or already visited cell
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            # Mark the cell as visited
            visit.add((r, c))
            # Recursively explore adjacent cells and count the area
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        # Initialize the maximum area to 0
        area = 0
        # Iterate through each cell in the grid
        for r in range(ROWS):
            for c in range(COLS):
                # If the cell is part of an unvisited island, find the area and update the maximum area
                area = max(area, dfs(r, c))
        # Return the maximum area of the island
        return area
