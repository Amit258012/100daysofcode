# https://leetcode.com/problems/min-cost-climbing-stairs/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The problem is a dynamic programming problem where the minimum cost to reach each step is calculated based on the minimum costs of the next two steps.
The backward iteration ensures that the minimum cost for each step is calculated with the updated values for subsequent steps.
"""


from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        # Iterate backward through the cost array starting from the third-to-last element.
        for i in range(n - 3, -1, -1):
            # Update the cost at the current step by adding the minimum cost of the next two steps.
            cost[i] += min(cost[i + 1], cost[i + 2])

        # The minimum cost to reach the top is the minimum of the first two elements in the updated cost array.
        return min(cost[0], cost[1])
