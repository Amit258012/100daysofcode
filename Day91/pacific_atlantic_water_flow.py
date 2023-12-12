# https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
Time complexity:- O(rows*cols) 
Space Complexity:- O(rows*cols)
"""

"""
Intuition:

DFS is used to traverse the matrix and explore reachable coordinates from the borders of the Pacific and Atlantic Oceans. The intersection of the two sets represents the coordinates where water can flow to both oceans.

Observation:

The dfs function recursively explores coordinates based on the given conditions.
The p_visited set stores coordinates reachable from the Pacific Ocean.
The a_visited set stores coordinates reachable from the Atlantic Ocean.
The intersection of these sets represents the common reachable coordinates.
"""
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return []

        # Get the number of rows and columns in the matrix
        m, n = len(matrix), len(matrix[0])

        # Sets to store visited coordinates for Pacific and Atlantic Oceans
        p_visited = set()
        a_visited = set()

        # Possible directions for water flow
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # Depth-First Search (DFS) function to explore the reachable coordinates
        def dfs(visited, x, y):
            visited.add((x, y))
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # Check if the new coordinates are within bounds and have not been visited
                # Also, check if the water can flow from the new coordinates to the current coordinates
                if (
                    0 <= new_x < m
                    and 0 <= new_y < n
                    and (new_x, new_y) not in visited
                    and matrix[new_x][new_y] >= matrix[x][y]
                ):
                    dfs(visited, new_x, new_y)

        # Iterate from the left and right borders for Pacific Ocean
        for i in range(m):
            dfs(p_visited, i, 0)
            dfs(a_visited, i, n - 1)

        # Iterate from the top and bottom borders for Pacific Ocean
        for j in range(n):
            dfs(p_visited, 0, j)
            dfs(a_visited, m - 1, j)

        # The intersections of the two sets are coordinates where water can flow to both Pacific and Atlantic Oceans
        return list(p_visited.intersection(a_visited))
