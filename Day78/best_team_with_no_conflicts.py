# https://leetcode.com/problems/best-team-with-no-conflicts/
"""
Time complexity:- O(N logN)
Space Complexity:- O(k) k=max(ages) 
"""

"""
Intuition:

The code addresses the problem of finding the maximum team score given the scores and ages of players.
Dynamic programming is used to efficiently calculate the maximum score for each age, considering the scores of players with the same age.
The 'dp' array is filled in a bottom-up manner, and at each step, the maximum score for the current age is updated based on the maximum scores of previous ages.
The final result is the overall maximum score, which is the maximum value in the 'dp' array.
"""
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # Initialize an array 'dp' to store the maximum scores for each age
        dp = [0] * (1 + max(ages))

        # Combine scores and ages, then sort by age
        score_age = sorted(zip(scores, ages))

        # Iterate through each player's score and age
        for score, age in score_age:
            # Update the maximum score for the current age
            dp[age] = score + max(dp[: age + 1])

        # Return the overall maximum score
        return max(dp)
