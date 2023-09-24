from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the number of rows and columns in the matrix
        n = len(matrix)
        m = len(matrix[0])

        # Start at the top-right corner (or bottom-left corner)
        row = 0
        col = m - 1

        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                # If the current element is smaller, move down in the same column
                row += 1
            else:
                # If the current element is larger, move left in the same row
                col -= 1

        return False  # Target not found in the matrix
