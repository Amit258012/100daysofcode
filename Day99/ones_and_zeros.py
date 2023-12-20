# https://leetcode.com/problems/ones-and-zeroes/
"""
Time complexity:- O(len(strs) * m * n)
Space Complexity:- O(m*n) 
"""

"""
Intuition:

The findMaxForm method uses dynamic programming to solve the 0/1 knapsack problem.
The DP array dp[i][j] represents the maximum number of strings that can be formed with i '0's and j '1's.
The counter list stores the count of '0's and '1's for each string in the input list strs.
The nested loops iterate through each string and update the DP array based on the counts of '0's and '1's, maximizing the count.
The result is obtained from the bottom-right cell of the DP array.
"""


from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D DP array with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Count the number of '0's and '1's in each string and store in the 'counter' list
        counter = [[s.count("0"), s.count("1")] for s in strs]

        # Iterate through each string in the 'strs' list
        for zeroes, ones in counter:
            # Iterate backward through the DP array to update counts
            for i in range(m, zeroes - 1, -1):
                for j in range(n, ones - 1, -1):
                    # Update the DP array with the maximum count
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones])

        # Return the maximum count from the bottom-right cell of the DP array
        return dp[-1][-1]
