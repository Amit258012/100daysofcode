"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
"""

"""
Time Complexity:- O(nlog(max[piles]))
Space Complexity:- o(1)
"""


class Solution:
    def calcTotalHr(self, piles, k):
        # Calculate the total hours required to eat all piles at a given speed 'k'.
        n = len(piles)
        totalHr = 0

        for i in range(n):
            # Use math.ceil to round up the hours for each pile.
            totalHr += math.ceil(piles[i] / k)

        return totalHr

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Find the maximum pile size as the upper bound for binary search.
        maxi = max(piles)

        # Initialize the low and high pointers for binary search.
        low = 1
        high = maxi

        while low <= high:
            mid = (low + high) // 2

            # Calculate the total hours required to eat all piles at the current speed 'mid'.
            totalhr = self.calcTotalHr(piles, mid)

            if totalhr <= h:
                # If total hours are less than or equal to 'h', reduce the eating speed (move left in binary search).
                high = mid - 1
            else:
                # If total hours exceed 'h', increase the eating speed (move right in binary search).
                low = mid + 1

        # Return the minimum eating speed found.
        return low
