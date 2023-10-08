# https://leetcode.com/problems/longest-common-prefix

"""
Time complexity:- O(nlogn + m)
Space Complexity:- O(1)
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""  # Initialize an empty string to store the common prefix
        v = sorted(strs)  # Sort the input list of strings lexicographically
        first = v[0]  # Get the first (smallest) string after sorting
        last = v[-1]  # Get the last (largest) string after sorting

        # Iterate through the characters of the smallest and largest strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans  # If a character mismatch is found, return the current common prefix
            ans += first[i]  # Append the character to the common prefix

        return ans  # Return the common prefix found
