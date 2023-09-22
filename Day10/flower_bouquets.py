"""
You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
"""

"""
Time Complexity:- O(nlog(min-max+1))
Space Complexity:- o(1)
"""


from typing import List


class Solution:
    def possible(self, bloomDay, day, m, k):
        count = 0
        no_of_bouquets = 0
        n = len(bloomDay)

        # Iterate through bloomDay to count the number of flowers that can be used to make bouquets each day.
        for i in range(n):
            if day >= bloomDay[i]:
                count += 1
            else:
                no_of_bouquets += (
                    count // k
                )  # Calculate the number of bouquets that can be made with 'k' flowers.
                count = (
                    0  # Reset the count because we can't make a bouquet on this day.
                )

        no_of_bouquets += (
            count // k
        )  # Calculate the remaining bouquets that can be made.

        # Return True if it's possible to make at least 'm' bouquets; otherwise, return False.
        return no_of_bouquets >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        h = max(bloomDay)
        n = len(bloomDay)

        # If it's not possible to make 'm' bouquets with 'k' flowers each (due to insufficient flowers), return -1.
        if m * k > n:
            return -1

        # Binary search for the minimum number of days required.
        while l <= h:
            mid = (l + h) // 2

            if self.possible(bloomDay, mid, m, k):
                h = mid - 1  # Adjust the upper bound for the binary search.
            else:
                l = mid + 1  # Adjust the lower bound for the binary search.

        # Return the minimum number of days needed to make 'm' bouquets.
        return l
