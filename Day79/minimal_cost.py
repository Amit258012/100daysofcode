# https://www.codingninjas.com/studio/problems/minimal-cost_8180930
"""
Time complexity:- O(N*k) k = maximum number of steps
Space Complexity:- O(N) 
"""

"""
Intuition:

The code addresses the problem of minimizing the cost of reaching the last position with a limited number of allowed steps.
Dynamic programming is utilized to efficiently calculate the minimum cost for each position by considering the costs of possible steps from previous positions.
The 'dp' array is filled in a bottom-up manner, and at each step, the minimum cost for reaching the current position is updated based on the costs of previous positions.
The final result is the minimum cost of reaching the last position, which is stored in the last element of the 'dp' array.
"""

from typing import List


def minimizeCost(n: int, k: int, height: List[int]) -> int:
    # Initialize an array 'dp' to store the minimum cost of reaching each position
    dp = [-float("inf")] * n
    dp[0] = 0

    # Iterate through each position starting from the second one
    for i in range(1, n):
        # Initialize the minimum cost of jumping 'j' steps to infinity (not a valid option initially)
        mmSteps = float("inf")

        # Iterate through possible steps 'j' (up to 'k')
        for j in range(1, k + 1):
            # Check if jumping 'j' steps from the current position is a valid option (not out of bounds)
            if i - j >= 0:
                # Calculate the cost of jumping 'j' steps and update the minimum cost
                jump = dp[i - j] + abs(height[i] - height[i - j])
                mmSteps = min(jump, mmSteps)

        # Store the minimum cost of reaching the current position in the 'dp' array
        dp[i] = mmSteps

    # The result is the minimum cost of reaching the last position
    return dp[n - 1]
