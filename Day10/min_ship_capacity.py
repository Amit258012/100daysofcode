"""
A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
"""

"""
Time Complexity:- O(nlog(sum-max+1))
Space Complexity:- o(1)
"""


class Solution:
    def findDays(self, weights, cap):
        load = 0
        days = 1
        n = len(weights)
        for i in range(n):
            if load + weights[i] > cap:
                days += 1
                load = weights[i]
            else:
                load += weights[i]
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        n = len(weights)

        while low <= high:
            mid = (low + high) // 2

            if self.findDays(weights, mid) <= days:
                high = mid - 1
            else:
                low = mid + 1
        return low
