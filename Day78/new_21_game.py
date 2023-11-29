# https://leetcode.com/problems/new-21-game/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The code addresses the problem of finding the probability of reaching a score within a certain range in a game where points are gained randomly.
Dynamic programming is utilized to efficiently calculate the probabilities for each score based on the given rules.
The 'dp' array is filled in a bottom-up manner, and at each step, the probability for the current score is calculated based on the probabilities of the previous scores.
The final result is the sum of probabilities for scores starting from 'k' to 'n', as those are the relevant scores for the problem.
"""
from typing import List


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Initialize an array 'dp' to store the probabilities of reaching each score
        dp = [0] * (n + 1)
        dp[0] = 1

        # Initialize a variable 's' to track the sum of probabilities for the last 'maxPts' scores
        s = 1 if k > 0 else 0

        # Iterate through each score from 1 to n
        for i in range(1, n + 1):
            # Calculate the probability for the current score
            dp[i] = s / maxPts

            # Update the sum for the last 'maxPts' scores
            if i < k:
                s += dp[i]

            # Subtract the probability of the score 'i - maxPts' if it is within the valid range
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]

        # Return the sum of probabilities for scores starting from 'k' to 'n'
        return sum(dp[k:])
