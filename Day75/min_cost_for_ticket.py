# https://leetcode.com/problems/minimum-cost-for-tickets/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The code addresses the problem of finding the minimum cost to travel on a given set of days using three types of passes (1-day, 7-day, and 30-day).
Dynamic programming is utilized to efficiently calculate the minimum cost for each day based on the costs of different passes and the minimum costs for previous days.
The 'dp' array is filled iteratively, and the final result is the minimum cost for the last day in the 'dp' array.
"""

from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Initialize an array 'dp' to store the minimum cost for each day
        dp = [0 for i in range(days[-1] + 1)]

        # Convert 'days' list to a set for faster lookup
        travel_days = set(days)

        # Iterate through each day
        for i in range(days[-1] + 1):
            # If the current day is not a travel day, copy the cost from the previous day
            if i not in travel_days:
                dp[i] = dp[i - 1]
            else:
                # Calculate the minimum cost for the current day using costs for 1-day, 7-day, and 30-day passes
                dp[i] = min(
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 1)] + costs[0],
                    dp[max(0, i - 30)] + costs[2],
                )

        # Return the minimum cost for the last day in 'dp'
        return dp[-1]
