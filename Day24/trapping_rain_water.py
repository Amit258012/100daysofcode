# https://leetcode.com/problems/trapping-rain-water/

"""
Time complexity:- O(n)
Space Complexity:- O(1)
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        ans = 0

        # using two pointers i and j on indices 1 and n-1
        l = 1
        r = len(height) - 1

        # initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]

        while l <= r:
            # check lmax and rmax for current i, j positions
            if height[l] > lmax:
                lmax = height[l]
            if height[r] > rmax:
                rmax = height[r]

            # fill water upto lmax level for index i and move i to the right
            if lmax <= rmax:
                ans += lmax - height[l]
                l += 1

            # fill water upto rmax level for index j and move j to the left
            else:
                ans += rmax - height[r]
                r -= 1

        return ans
