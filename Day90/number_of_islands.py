# https://leetcode.com/problems/number-of-islands/
"""
Time complexity:- O(rows*cols) 
Space Complexity:- O(rows*cols)
"""

"""
Intuition:

DFS is used to traverse the grid and explore connected land cells. The visit set ensures that each land cell is visited exactly once.

Observation:

The DFS function explores neighboring cells in all four directions.
The numIslands function iterates through each cell and initiates DFS for unvisited land cells, counting each initiation as the discovery of a new island.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid is empty
        if not grid or not grid[0]:
            return 0

        # Variables to keep track of islands count and visited cells
        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        # Depth-First Search (DFS) function
        def dfs(r, c):
            # Base cases for out-of-bounds or water cells
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            # Mark the current cell as visited
            visit.add((r, c))

            # Possible directions for DFS
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            # Explore neighbors in all directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterate through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If the cell is part of an unvisited island, initiate DFS
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)

        # Return the total count of islands
        return islands
