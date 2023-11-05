# https://leetcode.com/problems/merge-intervals/

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""


from typing import List


class Solution:
    def merge(self, itvs: List[List[int]]) -> List[List[int]]:
        # Sort the input intervals 'itvs' based on their start values.
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
                res[-1][1] = max(res[-1][1], itv[1])

        # Return the list of merged intervals 'res'.
        return res
