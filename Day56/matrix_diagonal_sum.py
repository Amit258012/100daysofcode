# https://leetcode.com/problems/matrix-diagonal-sum/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""


from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)  # Get the size of the square matrix
        diagonal_sum = 0  # Initialize the diagonal sum

        for i in range(n):
            diagonal_sum += mat[i][i]  # Add the elements of the primary diagonal
            diagonal_sum += mat[i][
                n - 1 - i
            ]  # Add the elements of the secondary diagonal

        # If the matrix has an odd size, subtract the center element to avoid double-counting
        if n % 2 == 1:
            center_index = n // 2
            diagonal_sum -= mat[center_index][center_index]

        return diagonal_sum  # Return the calculated diagonal sum
