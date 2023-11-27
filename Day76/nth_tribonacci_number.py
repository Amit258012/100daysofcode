# https://leetcode.com/problems/n-th-tribonacci-number/
"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

The code calculates the n-th Tribonacci number using a recursive approach with memoization.
Base cases are defined for n = 0, 1, and 2.
The result for each value of n is calculated by recursively summing the results for the three preceding values (n - 1, n - 2, n - 3).
Memoization is used to store and reuse previously calculated results, avoiding redundant computations and improving efficiency.
"""


class Solution:
    Memo = {}  # Class-level memoization dictionary

    def tribonacci(self, n: int) -> int:
        # Check if the result for n is already memoized
        if n in self.Memo:
            return self.Memo[n]

        # Base cases for n = 0, 1, 2
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        # Recursive call to calculate tribonacci(n) using memoization
        self.Memo[n] = (
            self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        )

        # Return the memoized result for tribonacci(n)
        return self.Memo[n]
