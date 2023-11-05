# https://leetcode.com/problems/insert-interval/

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""


from typing import List


class Solution:
    def insert(self, itvs: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Append the new interval to the list of intervals.
        itvs.append(newInterval)
        # Sort the intervals based on their start values.
        itvs = sorted(itvs, key=lambda x: x[0])
        # Initialize an empty list to store the merged intervals.
        res = []

        for itv in itvs:
            # If 'res' is empty or the end of the last interval in 'res' is less than the start of the current interval,
            # add the current interval to 'res'.
            if not res or res[-1][1] < itv[0]:
                res.append(itv)
            else:
                # If there is an overlap, merge the current interval with the last interval in 'res' by updating the end value.
                res[-1][1] = max(itv[1], res[-1][1])

        # Return the list of merged intervals 'res'.
        return res
