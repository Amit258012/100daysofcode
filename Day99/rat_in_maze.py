# https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1
"""
Time complexity:- O(3^(n^2))
Space Complexity:- O(n^2) 
"""

"""
Intuition:

The findPath method initializes the visited matrix and an empty list ans to store the paths.
The find method is a recursive function that explores all possible paths from the current cell to the destination.
The is_valid method checks if a cell is within the bounds of the maze, has not been visited before, and contains a 1.
When reaching the destination cell, the current path is appended to the ans list.
The solution explores all possible paths using backtracking.
"""


class Solution:
    def is_valid(self, i, j, m, n, visited):
        """
        Check if the cell (i, j) is a valid cell to move to.
        """
        if (
            i < n
            and j < n
            and i >= 0
            and j >= 0
            and visited[i][j] == 0
            and m[i][j] == 1
        ):
            return True
        return False

    def find(self, i, j, m, n, visited, path, ans):
        """
        Recursively find all paths from the starting cell (0, 0) to the destination cell (n-1, n-1).
        """
        if i == n - 1 and j == n - 1 and m[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] == 1
            ans.append(path)

        if self.is_valid(i, j, m, n, visited):
            visited[i][j] = 1
            self.find(i + 1, j, m, n, [x[:] for x in visited], path + "D", ans)
            self.find(i, j - 1, m, n, [x[:] for x in visited], path + "L", ans)
            self.find(i, j + 1, m, n, [x[:] for x in visited], path + "R", ans)
            self.find(i - 1, j, m, n, [x[:] for x in visited], path + "U", ans)

    def findPath(self, m, n):
        """
        Find all possible paths from the top-left corner to the bottom-right corner in a maze.
        """
        visited = [[0 for i in range(n)] for i in range(n)]
        ans = []
        self.find(0, 0, m, n, [x[:] for x in visited], "", ans)
        return ans
