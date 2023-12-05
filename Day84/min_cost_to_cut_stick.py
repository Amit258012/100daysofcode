# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
"""
Time complexity:- O(N^3)
Space Complexity:- O(N^2)
"""

"""
Intuition:

The algorithm uses dynamic programming to find the minimum cost of cutting the given segment.
The 'cuts' array is extended with 0 and 'n' to include the endpoints.
The 'dp' array is used to store the minimum cost of cutting subsegments.
The algorithm iterates over all possible subsegments and calculates the cost of cutting at each midpoint, updating the minimum cost.
The result is the minimum cost of cutting the entire segment, stored in 'dp[0][m + 1]'.
"""


from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Append 0 and 'n' to the 'cuts' list to include the endpoints
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        # Initialize a 2D array 'dp' to store the minimum cost of cutting subsegments
        dp = [[0] * (m + 2) for _ in range(m + 2)]

        # Iterate over the possible differences between left and right cuts
        for diff in range(2, m + 2):
            # Iterate over the left cuts
            for left in range(m + 2 - diff):
                right = left + diff
                ans = float("inf")

                # Iterate over possible midpoints between left and right cuts
                for mid in range(left + 1, right):
                    # Calculate the cost of cutting the subsegment at the midpoint
                    # and update the minimum cost
                    ans = min(
                        ans, dp[left][mid] + dp[mid][right] + cuts[right] - cuts[left]
                    )

                # Update the dp array with the minimum cost for the current subsegment
                dp[left][right] = ans

        # The result is the minimum cost of cutting the entire segment
        return dp[0][m + 1]
