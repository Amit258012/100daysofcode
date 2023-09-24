from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        low = 0
        high = n * m - 1

        while low <= high:
            mid = (low + high) // 2
            rowCount = mid // m
            colCount = mid % m

            if matrix[rowCount][colCount] == target:
                return True
            elif matrix[rowCount][colCount] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
