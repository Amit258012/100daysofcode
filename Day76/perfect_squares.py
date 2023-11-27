# https://leetcode.com/problems/perfect-squares/
"""
Time complexity:- O(N. N^(1/2))
Space Complexity:- O(N) 
"""

"""
Intuition:

The code addresses the problem of finding the minimum number of perfect squares that sum to a given number n.
Dynamic programming is utilized to efficiently calculate the minimum number of perfect squares for each value up to n.
The 'dp' array is iteratively filled, considering the possibilities of using each perfect square less than or equal to the current value of i.
The final result is the minimum number of perfect squares needed to sum to n, which is stored in dp[-1].
"""


class Solution:
    def numSquares(self, n: int) -> int:
        # Step 1: Initialize a list 'dp' to store the minimum number of perfect squares for each value up to n.
        dp = [i for i in range(n + 1)]

        # Step 2: Iterate over each number from 0 to n.
        for i in range(n + 1):
            j = 1

            # Step 3: While the square of j is less than or equal to i, update dp[i] with the minimum value.
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - (j * j)] + 1)
                j += 1

        # Return the result for n, which is stored at dp[-1].
        return dp[-1]
