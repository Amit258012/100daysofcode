# https://leetcode.com/problems/coin-change-ii/
"""
Time complexity:- O(c * a), where c is the number of coins and a is the given amount.
Space Complexity:- O(a)
"""

"""
Intuition:

The code addresses the problem of finding the number of ways to make change for a given amount using a given set of coins.
Dynamic programming is utilized to efficiently calculate the number of ways to make change for each amount.
The 'dp' array is filled in a bottom-up manner, and at each step, the number of ways to make change for the current amount is updated based on the values for smaller amounts.
The final result is the number of ways to make change for the given amount, which is stored in the last element of the 'dp' array.
"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize an array 'dp' to store the number of ways to make change for each amount
        dp = [0] * (amount + 1)
        # There is one way to make change for the amount of 0 (using no coins)
        dp[0] = 1

        # Iterate through each coin in the list
        for coin in coins:
            # Iterate through each amount starting from 'coin'
            for j in range(coin, amount + 1):
                # Update the number of ways to make change for the current amount
                dp[j] += dp[j - coin]

        # The result is the number of ways to make change for the given amount
        return dp[amount]
