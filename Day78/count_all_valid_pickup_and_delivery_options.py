# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/
"""
Time complexity:- O(N)
Space Complexity:- O(1)
"""

"""
Intuition:

The code addresses the problem of counting the number of different orders in which a customer can purchase n products.
The formula used to calculate the result is based on permutations and combinations, considering the choices for each product in the order.
The result is updated in a loop for each value from 2 to n, and the final result is returned after the loop.
Note: The final result is converted to an integer before returning.
"""


class Solution:
    def countOrders(self, n: int) -> int:
        # Initialize the result and modulo
        res, mod = 1, 10**9 + 7

        # Iterate from 2 to n
        for i in range(2, n + 1):
            # Update the result by multiplying with (i * 2 - 1) * (i * 2) / 2 and taking modulo
            res = res * (i * 2 - 1) * (i * 2) / 2 % mod

        # Convert the result to an integer before returning
        return int(res)
