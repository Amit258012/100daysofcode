# https://leetcode.com/problems/rotting-oranges/
"""
Time complexity:- O(N) 
Space Complexity:- O(N)
"""

"""
Intuition:

The algorithm uses Breadth-First Search (BFS) to simulate the rotting process, starting from initially rotten oranges.
The queue (q) is used to keep track of the rotten oranges and their coordinates.
The process continues until either all fresh oranges are rotten or there are no more rotten oranges.
The time variable keeps track of the minutes passed during the rotting process.
If there are still fresh oranges after the simulation, it means some oranges cannot be rotten, and -1 is returned.
The algorithm follows a simple and intuitive approach of simulating the rotting process through BFS traversal.
"""
import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()  # Using deque for efficient pop and append operations
        fresh = 0  # Counter for fresh oranges
        time = 0  # Variable to track time (minutes)

        # Iterate through the grid to identify fresh and rotten oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))  # Add coordinates of rotten oranges to the queue

        # Directions to check neighboring cells (up, down, left, right)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        # BFS traversal to simulate rotting process
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()  # Pop the front of the queue

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    # Check if the neighboring cell is in bounds and contains a fresh orange
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        grid[row][col] = 2  # Mark the orange as rotten
                        q.append((row, col))  # Add the coordinates to the queue
                        fresh -= 1  # Decrease the count of fresh oranges

            time += 1  # Increment time after processing each minute

        # Return the time required if all fresh oranges are rotten, otherwise return -1
        return time if fresh == 0 else -1
