# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
"""
Time complexity:- O(2^N)
Space Complexity:- O(N)
"""

"""
Intuition:

The code addresses the problem of finding the maximum profit that can be obtained by buying and selling stocks.
Dynamic programming with memoization is used to avoid redundant calculations and improve efficiency.
The recursive function ('dfs') explores all possible decisions at each step: either buying or not buying the stock.
The final result is the maximum profit that can be obtained starting from the first day with an initial buying decision.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Dictionary to memoize results of subproblems: key=(i, buying), value=max_profit
        dp = {}

        # Recursive function to explore all possible buying and selling decisions
        def dfs(i, buying):
            # Base case: if we have reached the end of the prices array
            if i >= len(prices):
                return 0

            # Check if the result for the current subproblem is already memoized
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Recursive calls for the two possible decisions: buying or not buying
            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            # Return the result for the current subproblem
            return dp[(i, buying)]

        # Start the recursive process from the first day with an initial buying decision
        return dfs(0, True)
