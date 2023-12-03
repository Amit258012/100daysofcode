# https://leetcode.com/problems/minimum-number-of-coins-to-be-added/
"""
Time complexity:- O(NlogN)
Space Complexity:- O(1)
"""

"""
Intuition:

The code aims to find the minimum number of coins needed to reach a target value using a set of given coins.
It does this by iteratively extending the maximum possible sum using the available coins and adding extra coins when necessary.
The algorithm handles the sorted coins in ascending order and adjusts the maximum possible sum to cover the target value.
"""
from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        # Sort the coins in ascending order
        coins.sort()

        # Initialize variables to track the maximum possible sum and minimum coins needed
        max_possible_sum = 0
        min_coins_needed = 0

        # Iterate through the sorted coins
        for coin in coins:
            # Check if the current coin can be used to extend the maximum possible sum
            if coin <= max_possible_sum + 1:
                max_possible_sum += coin
            else:
                # Add coins to reach the next reachable value and update the minimum coins needed
                while coin > max_possible_sum + 1:
                    max_possible_sum = 2 * max_possible_sum + 1
                    min_coins_needed += 1
                max_possible_sum += coin

        # Add coins to reach the target value and update the minimum coins needed
        while target > max_possible_sum:
            max_possible_sum = 2 * max_possible_sum + 1
            min_coins_needed += 1

        # Return the minimum coins needed to reach the target value
        return min_coins_needed
