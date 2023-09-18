"""
        Rotate the given NxN matrix 90 degrees clockwise in-place.

        Args:
            matrix (List[List[int]]): The input matrix to be rotated.

        Returns:
            None: The function modifies the 'matrix' in-place and does not return anything.
"""
"""
Time Complexity:- O(n^2)
Space Complexity:- O(1)
"""


class Solution:
    def rotate(self, matrix):
        # Reverse the matrix vertically (upside down).
        matrix.reverse()

        # Transpose the reversed matrix to rotate it 90 degrees clockwise.
        # This swaps elements along the main diagonal (top-left to bottom-right).
        for i in range(len(matrix)):
            for j in range(i):
                # Swap elements at position (i, j) and (j, i).
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
