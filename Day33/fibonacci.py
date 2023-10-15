# https://leetcode.com/problems/fibonacci-number/

"""
Time complexity:- O(2^n)
Space Complexity:- O(n)
"""


class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n  # Base case: Fibonacci numbers for n=0 and n=1 are 0 and 1.

        # Recursive case: Calculate the nth Fibonacci number by summing the (n-1)th and (n-2)th Fibonacci numbers.
        return self.fib(n - 1) + self.fib(n - 2)
