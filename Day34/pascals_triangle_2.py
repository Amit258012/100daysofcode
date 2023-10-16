# https://leetcode.com/problems/pascals-triangle-ii/

"""
Time complexity:- O(n^2)
Space Complexity:- O(n)
"""
from types import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Create a list for the current row and initialize it with 1's.
        row = [1] * (rowIndex + 1)

        # Base case: If rowIndex is 0, return the row with a single element (1).
        if rowIndex == 0:
            return row

        # Recursively compute the previous row.
        prev_row = self.getRow(rowIndex - 1)

        # Compute the values for the current row based on the previous row.
        for i in range(1, len(row) - 1):
            row[i] = prev_row[i - 1] + prev_row[i]

        return row
