# https://leetcode.com/problems/longest-turbulent-subarray/

"""
Time complexity:- O(N)
Space Complexity:- O(1) 
"""

"""
Intuition:

The code uses two pointers (l and r) to iterate through the array, checking for turbulent relationships.
It keeps track of the result (res) and the direction of the previous comparison (prev).
Whenever a turbulent relationship is found, it updates the result and moves the right pointer (r).
If not in a turbulent relationship, it updates the pointers accordingly.
"""


from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Initialize pointers and variables to track result and previous comparison.
        l, r = 0, 1
        res, prev = 1, ""

        # Iterate through the array to find the maximum turbulent subarray size.
        while r < len(arr):
            # Check if the current pair is in a turbulent relationship (increasing).
            if arr[r - 1] > arr[r] and prev != ">":
                res = max(res, r - l + 1)
                r += 1
                prev = ">"
            # Check if the current pair is in a turbulent relationship (decreasing).
            elif arr[r - 1] < arr[r] and prev != "<":
                res = max(res, r - l + 1)
                r += 1
                prev = "<"
            # If not in a turbulent relationship, update pointers accordingly.
            else:
                r = r + 1 if arr[r] == arr[r - 1] else r
                l = r - 1
                prev = ""

        # Return the maximum turbulent subarray size.
        return res
