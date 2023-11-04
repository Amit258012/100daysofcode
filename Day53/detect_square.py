# https://leetcode.com/problems/detect-squares/

"""
Time complexity:- O(1) O(1) O(N)
Space Complexity:- O(N) 
"""

from collections import defaultdict
from typing import List


class DetectSquares:
    def __init__(self):
        # Initialize a defaultdict to count the occurrences of each point.
        self.ptsCount = defaultdict(int)
        # Initialize a list to store all the added points.
        self.pts = []

    def add(self, point: List[int]) -> None:
        # Increment the count for the given point in ptsCount.
        self.ptsCount[tuple(point)] += 1
        # Append the point to the list of all points.
        self.pts.append(point)

    def count(self, point: List[int]) -> int:
        # Initialize a variable to store the count of squares.
        res = 0
        px, py = point  # Extract the coordinates of the provided point.

        # Iterate over all points in the pts list.
        for x, y in self.pts:
            # Check if the conditions for forming a square are met:
            # 1. The absolute difference between px-x is equal to the absolute difference between py-y.
            # 2. The x and y coordinates are not equal to px and py, respectively.
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue

            # Calculate the count of points [x, py] (horizontal side) and [px, y] (vertical side)
            # using the ptsCount dictionary.
            horizontal_side_count = self.ptsCount[(x, py)]
            vertical_side_count = self.ptsCount[(px, y)]

            # Multiply the two counts and add the result to the total count of squares.
            res += horizontal_side_count * vertical_side_count

        # Return the total count of squares that can be formed with the provided point.
        return res
