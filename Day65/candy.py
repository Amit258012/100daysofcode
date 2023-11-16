# https://leetcode.com/problems/candy/

"""
Time complexity:- O(N)
Space Complexity:- O(N) 
"""

"""
Intuition:

First iteration (left to right): Assign candies to children based on the increasing trend in ratings.
Second iteration (right to left): Adjust candies for cases where the ratings decrease from right to left.
The approach ensures that the final distribution satisfies both increasing and decreasing trends in ratings. The sum of candies represents the minimum required to achieve this distribution.
"""

from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Get the number of children
        n = len(ratings)
        # Initialize an array to store the number of candies each child gets
        candies = [1] * n

        # Traverse the ratings array from left to right
        for i in range(1, n):
            # If the current child's rating is higher than the previous one, give more candies
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Traverse the ratings array from right to left
        for i in range(n - 2, -1, -1):
            # If the current child's rating is higher than the next one, adjust candies
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return the total number of candies needed
        return sum(candies)
