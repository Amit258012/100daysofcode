# https://leetcode.com/problems/counting-bits/

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize a list 'dp' to store the number of 1 bits for each integer from 0 to 'n'.
        dp = [0] * (n + 1)
        offset = 1  # Initialize an 'offset' variable to keep track of the power of 2.

        # Iterate through integers from 1 to 'n'.
        for i in range(1, n + 1):
            # Check if 'i' is a power of 2, in which case update the 'offset'.
            if offset * 2 == i:
                offset = i
            # Calculate the number of 1 bits for 'i' using 'offset'.
            dp[i] = 1 + dp[i - offset]

        return dp  # Return the list 'dp' containing the counts.
