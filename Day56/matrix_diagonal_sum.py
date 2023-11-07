# https://leetcode.com/problems/matrix-diagonal-sum/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""


from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)  # Get the size of the square matrix
        diagonalSum = 0  # Initialize the diagonal sum

        for i in range(n):
            # Add the elements of the primary diagonal
            diagonalSum += mat[i][i]
            # Add the elements of the secondary diagonal
            diagonalSum += mat[i][n - 1 - i]

        # If the matrix has an odd size, subtract the center element to avoid double-counting
        if n % 2 == 1:
            centerIndex = n // 2
            diagonalSum -= mat[centerIndex][centerIndex]

        return diagonalSum  # Return the calculated diagonal sum
