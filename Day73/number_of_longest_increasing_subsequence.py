# https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""
Time complexity:- O(N^2)
Space Complexity:- O(N) 
"""

"""
Intuition:

The code aims to find the number of Longest Increasing Subsequences (LIS) in the given array.
Dynamic programming is used to efficiently calculate the length and count of LIS starting from each index, storing results in the dp dictionary.
The intuition is to iteratively explore and update the counts of LIS for each index, considering the elements to the right of the current index. The final result is the count of LIS for the entire array.
"""


from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}  # Dictionary to store results for dynamic programming
        lenLIS, res = 0, 0  # Initialize length of LIS and count of LIS

        # Iterate over the indices in reverse order
        for i in range(len(nums) - 1, -1, -1):
            # Initialize length and count of LIS starting from index i
            maxLen, maxCnt = 1, 1

            # Iterate over indices after i
            for j in range(i + 1, len(nums)):
                # Check if the current element can be part of the increasing subsequence
                if nums[j] > nums[i]:
                    length, count = dp[j]  # Length and count of LIS starting from j
                    # Update maxLen and maxCnt if a longer LIS is found
                    if length + 1 > maxLen:
                        maxLen, maxCnt = length + 1, count
                    elif length + 1 == maxLen:
                        maxCnt += count

            # Update the global length and count of LIS
            if maxLen > lenLIS:
                lenLIS, res = maxLen, maxCnt
            elif maxLen == lenLIS:
                res += maxCnt

            # Store the result for the current index in the dp dictionary
            dp[i] = [maxLen, maxCnt]

        # Return the final count of LIS
        return res
