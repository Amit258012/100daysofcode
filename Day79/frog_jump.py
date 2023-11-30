# https://www.codingninjas.com/studio/problems/frog-jump_3621012
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The code addresses the problem of finding the minimum cost of reaching the last position in a frog jump scenario.
The algorithm iteratively calculates the cost of jumping one or two positions and chooses the minimum cost at each position.
Two variables, 'prev' and 'prev2', are used to store the minimum costs of reaching the previous two positions.
The final result is the minimum cost of reaching the last position, which is stored in the 'prev' variable.
"""

from typing import List


def frogJump(n: int, height: List[int]) -> int:
    # Initialize variables to track the minimum cost of reaching each position
    prev = 0
    prev2 = 0

    # Iterate through each position starting from the second one
    for i in range(1, n):
        # Initialize the cost of jumping two positions to infinity (not a valid option initially)
        jumpTwo = float("inf")

        # Calculate the cost of jumping one position from the previous position
        jumpOne = prev + abs(height[i] - height[i - 1])

        # Check if jumping two positions is a valid option (not out of bounds)
        if i > 1:
            jumpTwo = prev2 + abs(height[i] - height[i - 2])

        # Choose the minimum cost for reaching the current position
        cur_i = min(jumpOne, jumpTwo)

        # Update variables for the next iteration
        prev2 = prev
        prev = cur_i

    # The result is the minimum cost of reaching the last position
    return prev
