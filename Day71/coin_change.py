# https://leetcode.com/problems/coin-change/
"""
Time complexity:- O(N * noOfCoins) N = amount
Space Complexity:- O(N) 
"""

"""
Intuition:

The coinChange function uses dynamic programming to find the minimum number of coins needed to make up a given amount.
It iterates through each amount and each coin denomination to update the minimum number of coins required.
"""


from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize a dynamic programming array to store the minimum number of coins needed for each amount.
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Iterate through amounts from 1 to the target amount.
        for a in range(1, amount + 1):
            # Iterate through each coin denomination.
            for c in coins:
                # Check if the current coin can be used to form the current amount.
                if a - c >= 0:
                    # Update the minimum number of coins needed for the current amount.
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # Return the minimum number of coins needed for the target amount.
        # If it's still the initial value (amount + 1), it means no valid combination exists.
        return dp[amount] if dp[amount] != amount + 1 else -1
