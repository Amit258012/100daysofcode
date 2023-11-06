# https://leetcode.com/problems/non-overlapping-intervals/

"""
Time complexity:- O(NlogN)
Space Complexity:- O(1) 
"""

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals based on their start values.
        intervals.sort()

        res = 0  # Initialize the count of overlapping intervals.
        prevEnd = intervals[0][1]  # Initialize the end time of the first interval.

        # Iterate through the sorted intervals, starting from the second interval.
        for start, end in intervals[1:]:
            if start >= prevEnd:
                # If the start of the current interval is greater than or equal to the previous end, they do not overlap.
                # Update the previous end to the end of the current interval.
                prevEnd = end
            else:
                # If they overlap, increment the count of overlapping intervals.
                res += 1
                # Update the previous end to the minimum of the previous end and the end of the current interval.
                prevEnd = min(prevEnd, end)

        return res  # Return the count of overlapping intervals that need to be removed.
