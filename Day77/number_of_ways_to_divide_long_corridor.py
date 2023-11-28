# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/
"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code addresses the problem of finding the number of ways to traverse a corridor with three possible moves ('L', 'R', and 'S').
The variables zero, one, and two are used to keep track of the number of ways to reach the current position after making zero, one, and two 'S' moves, respectively.
The algorithm iterates through each character in the corridor, updating the variables based on the current character ('S' or 'L' or 'R').
The final result is the number of ways to traverse the corridor with zero 'S' moves, which is stored in the 'zero' variable.
"""
from typing import List


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        # Store 1000000007 in a variable for convenience
        MOD = 1_000_000_007

        # Initial values of three variables
        zero = 0
        one = 0
        two = 1

        # Iterate through each character in the corridor
        for thing in corridor:
            if thing == "S":
                # Update values based on the presence of 'S'
                zero = one
                one, two = two, one
            else:
                # Update 'two' by adding 'zero', and take modulo to prevent overflow
                two = (two + zero) % MOD

        # The result is the value of 'zero'
        return zero
