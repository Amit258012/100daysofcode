# https://leetcode.com/problems/two-city-scheduling/

"""
Time complexity:- O(N logN)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code sorts the costs based on the difference between the costs for city A and city B.
It then assigns the first half of the sorted costs to city A and the second half to city B.
The total cost for both cities is calculated and returned.
"""

from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort the costs based on the difference between costs for city A and city B.
        sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])

        # Initialize costs for city A and city B.
        total_cost_A = 0
        total_cost_B = 0

        # Iterate through the first half of the sorted costs, assigning to city A.
        for i in range(len(sorted_costs) // 2):
            total_cost_A += sorted_costs[i][0]

        # Iterate through the second half of the sorted costs, assigning to city B.
        for i in range(len(sorted_costs) // 2, len(sorted_costs)):
            total_cost_B += sorted_costs[i][1]

        # Return the total cost for both cities.
        return total_cost_A + total_cost_B
