# https://leetcode.com/problems/binary-subarrays-with-sum/
"""
Time complexity:- O(N)
Space Complexity:- O(N)
"""

"""
Intuition:

The algorithm utilizes a prefix sum approach to efficiently find subarrays with the given sum ('goal').
It maintains a dictionary to store the counts of encountered prefix sums.
The key insight is to check for the presence of a specific prefix sum ('cur_sum - goal') in the dictionary, allowing us to count valid subarrays efficiently.
The algorithm updates the dictionary as it iterates through the array, incrementing counts for each encountered prefix sum.
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0  # Initialize the result variable to count subarrays

        prefix_sum = {0: 1}  # Use a dictionary to store prefix sums and their counts
        cur_sum = 0  # Initialize the current sum variable

        for num in nums:
            cur_sum += num  # Update the current sum with the current number

            # Check if there is a prefix sum 'cur_sum - goal' in the dictionary
            if cur_sum - goal in prefix_sum:
                # Increment the result with the count of valid subarrays
                res += prefix_sum[cur_sum - goal]

            # Update the dictionary with the current prefix sum
            if cur_sum not in prefix_sum:
                prefix_sum[cur_sum] = 1
            else:
                prefix_sum[cur_sum] += 1

        return res
