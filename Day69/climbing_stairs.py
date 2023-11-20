# https://leetcode.com/problems/climbing-stairs/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The problem represents a classic example of a Fibonacci sequence, where the number of ways to climb each step depends on the previous two steps.
The dynamic programming approach uses an array to store the solutions for subproblems, avoiding redundant calculations.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cases: there is one way to climb 0 or 1 step.
        if n == 0 or n == 1:
            return 1

        # Initialize an array to store the number of ways to climb up to each step.
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1  # Base cases for 0 and 1 steps.

        # Iterate from step 2 to n, calculating the number of ways for each step.
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
