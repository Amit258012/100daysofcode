# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

"""
Time complexity:- O(NlogN)
Space Complexity:- O(1) 
"""

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Check if the 'points' list is empty
        if not points:
            return 0

        # Sort the 'points' list based on the end coordinates in ascending order
        points.sort(key=lambda x: x[1])

        arrows = 1  # Initialize the number of arrows needed to 1
        first_end = points[0][1]  # Initialize the end coordinate of the first balloon

        # Iterate through the sorted 'points' list
        for x_start, x_end in points:
            # If the current balloon starts after the end of another one,
            # it requires one more arrow
            if first_end < x_start:
                arrows += 1
                first_end = x_end

        return arrows
